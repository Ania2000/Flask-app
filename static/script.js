function addMovie() {
var movieTitle = document.getElementById("InputTitle").value;
var movieYear = document.getElementById("InputYear").value;
var movieActor = document.getElementById("InputActor").value;

if (movieTitle === "") {
    alert("Movie title cannot be empty");
    return;

}
if (movieYear === "") {
    alert("Movie title cannot be empty");
    return;

}
if (movieActor === "") {
    alert("Movie title cannot be empty");
    return;

}
var li = document.createElement("li");
li.innerHTML = "<input type='checkbox'> " + movieTitle + ", " + movieYear + ", " + movieActor;
document.getElementById("MovieList").appendChild(li);

alert("MovieTitle");
console.log("MovieTitle");
}