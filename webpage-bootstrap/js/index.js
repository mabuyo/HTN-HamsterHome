var ref = new Firebase("https://hamster-home.firebaseio.com/");
var dateRef = new Firebase("https://hamster-home.firebaseio.com/last_updated");

// set references to components
var foodRef = new Firebase("https://hamster-home.firebaseio.com/food");
var waterRef = new Firebase("https://hamster-home.firebaseio.com/water");
var wheelRef = new Firebase("https://hamster-home.firebaseio.com/wheel");

/** WATER FUNCTIONS **/
waterRef.on('value', function(snapshot) {
	console.log(snapshot.val());
	var water = snapshot.val();
	$('.water-status').each(function() { 
		if (water.isFull == true) {
			console.log("Water status: full");
			$(this).html("Full");
		} else {
			console.log("Water status: empty");
			$(this).html("Empty");
		}
	});
});	

/** FOOD FUNCTIONS **/
var date_lastFilled;

// food database changes
foodRef.on('child_added', function(childSnapshot, prevChildKey) {
	date_lastFilled = childSnapshot.val();
	console.log("Last date added: ", date_lastFilled);
	changeFoodStats();
	
});

function changeFoodStats() {
	console.log("Date last filled:", date_lastFilled.date);
	$('.food-status').each(function() { 
		$(this).html(date_lastFilled.date);
	});	
	
	// someone fed them
	$('.quick-food-status').each(function() {
		$(this).html("Recently fed");
	});
	$('.food-status').each(function() { 
		$(this).html((new Date(date_lastFilled.date)).toDateString() + " " + (new Date(date_lastFilled.date)).toTimeString().substring(0,8));
	});
}

// what happens when feed button is clicked? database is updated with the time it was fed.
$('.feedButton').on('click', function() {
	console.log("Feed button clicked!");
	foodRef.push({
		"date": new Date().toString()
	});
});

/** ALL TRACKED CHANGES **/
function trackChanges(){
	console.log("Tracking changes...");
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

function init() {
	// listeners
	console.log("initiating listeners");
	$('.update-stats').on('click', function() {
		trackChanges();
	});
}

//FIREBASE DATA INITALIZERS 
dateRef.once("value", function(data) {
	$('.last-update-date').each(function() {
		console.log(data.val());
		var d = data.val();
		$(this).html((new Date(d)).toDateString());
	});
});

init();

//wheel database changes


