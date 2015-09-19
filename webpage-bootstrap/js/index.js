var database = new Firebase("https://hamster-home.firebaseio.com/");

database.set({
  food: {},
  water: {
  	isFull: true
  },
  wheel: {}
});