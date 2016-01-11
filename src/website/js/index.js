var ref = new Firebase("https://hamster-home.firebaseio.com/");

// set references to components
var dateRef = new Firebase("https://hamster-home.firebaseio.com/last_updated");
var foodRef = new Firebase("https://hamster-home.firebaseio.com/food");
var waterRef = new Firebase("https://hamster-home.firebaseio.com/water");
var wheelRef = new Firebase("https://hamster-home.firebaseio.com/wheel");
var activityRef = new Firebase("https://hamster-home.firebaseio.com/activity");

/** WATER FUNCTIONS **/
waterRef.on('value', function(snapshot) {
	$('.water-status').each(function() {
		$(this).html(snapshot.val().stats);
	});
});	

/** WHEEL FUNCTIONS */
wheelRef.on('child_changed', function(snapshot) {
	$('#distance-stat').html(Math.floor(snapshot.val().totalDailyDistance) + " m");
});	

/** FOOD FUNCTIONS **/
var date_lastFilled;

// food database changes
foodRef.on('child_added', function(childSnapshot, prevChildKey) {
	date_lastFilled = childSnapshot.val();
	//console.log("Last date added: ", date_lastFilled);
	changeFoodStats();
});

foodRef.once('child_added', function(snapshot, prevChildKey) {
	console.log(snapshot.val());
	date_lastFilled = snapshot.val();
	changeFoodStats();
});

function changeFoodStats() {
	//console.log("Date last filled:", date_lastFilled.date);
	
	// hamster has been fed
	$('.quick-food-status').each(function() {
		$(this).html("recently fed");
	});
	$('.food-status').each(function() { 
		$(this).html((new Date(date_lastFilled.date)).toDateString() + " " + (new Date(date_lastFilled.date)).toTimeString().substring(0,8));
	});

}

// what happens when feed button is clicked? database is updated with the time it was fed.
// also pushes an activity
$('.feedButton').on('click', function() {	
	console.log("Feed button clicked!");
	// send f to refillFood for Arduino
	ref.child('refillFood').set({"refillFood":"f"});

	// log a food refill data point
	foodRef.push({
		"date": new Date().toString()
	});
	// log an activity notification
	activityRef.push({
		"date": new Date().toString(),
		"category": "food",
		"description": "Food refilled."
	});
	
});

/** ALL TRACKED CHANGES **/
function trackChanges(){
	console.log("Tracking changes...");
	// water
	var oldWaterStatus = $('.water-status').html();
	console.log("oldWaterStatus ", oldWaterStatus);
	console.log(waterRef.stats);
	if (oldWaterStatus !== waterRef.stats) {
		console.log('water has changed!');
		$('.water-status').each(function() {
			$(this).html(waterRef.stats);
		});
	}
	
	// food
	var currentDate = new Date();
	var timePassed = currentDate.getTime() - (new Date(date_lastFilled.date)).getTime();
	console.log("Time passed since last fed: ", timePassed.toString());
	if (timePassed < 2000) {
		$('.quick-food-status').each(function() {
			$(this).html("Recently fed");
		});
	} else if ((timePassed > 2000) && (timePassed < 120000)) {
		$('.quick-food-status').each(function() {
			$(this).html("A little hungry");
		});
	} else {
		$('.quick-food-status').each(function() {
			$(this).html("Needs food");
		});
	}
}

// camera stuff
function startCamera() {
	//console.log("Starting camera...");
	var canvas = document.getElementById("video-stream");
	var context = canvas.getContext("2d");

    if (context) {
      	var piImage = new Image();

    	piImage.onload = function() {
			//console.log('Drawing image');
			context.drawImage(piImage, 0, 0, canvas.width, canvas.height);      
		}

     	piImage.src = "http://192.168.0.28/picam/cam_pic.php?time=" + new Date().getTime();
    }

    requestAnimationFrame(startCamera);
}

function init() {
	// listeners
	console.log("initiating listeners");
	$('.update-stats').on('click', function() {
		trackChanges();
	});

	// camera video-stream
	//startCamera();
}

//FIREBASE DATA INITALIZERS 
dateRef.on("value", function(data) {
	$('.last-update-date').each(function() {
		//console.log(data.val());
		var d = data.val();
		$(this).html((new Date(d)).toDateString());
	});
});

wheelRef.once("value", function(data) {
	var currentDate = new Date();
	var month = currentDate.getMonth() + 1;
	var day = currentDate.getDate();
	var year = currentDate.getFullYear();
	var dateKey = (month+'-'+day+'-'+year).toString()
	// console.log((month+'-'+day+'-'+year).toString());
	// console.log(data.val()[dateKey].totalDailyDistance);
	// var initDistance = data.val()[dateKey].totalDailyDistance;

	// $('#distance-stat').html(Math.floor(initDistance) + " m");
});

activityRef.limitToLast(7).on('child_added', function (snapshot, prevChildKey) {
	var act = snapshot.val();
	var description = act.description;
	var date = act.date;
	var icon;
	switch (act.category) {
		case "water":
			icon = "fa-tint";
			break;
		case "food":
			icon = "fa-cutlery";
			break;
		case "wheel":
			icon = "fa-car";
			break;
		default:
			icon = "fa-bolt";
	}
	$("#activities-short").prepend('<a href="#" class="list-group-item"><i class="fa ' + icon +  ' fa-fw"></i>' + description +'<span class="pull-right text-muted small"><em>' + (new Date(date)).toDateString() + '</em></span></a>'
	);
});

init();

//wheel database changes


