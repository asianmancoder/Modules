/* 
This isn't really one of 'my' modules, but this is something that I learned on Khan Academy.
*/

var Walker = function() {
    this.x = width/2;
    this.y = height/2;
};

Walker.prototype.display = function() {
    stroke(0, 0, 0);
    point(this.x, this.y);
};

Walker.prototype.walk = function() {
    var choice = floor(random(4));
    if (choice === 0) {
        this.x++;
    } else if (choice === 1) {
        this.x--;
    } else if (choice === 2) {
        this.y++;
    } else {
        this.y--;
    } 
};
