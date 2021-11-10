  function Rocket(dna) {
    if (dna) {
      this.dna = dna;
    } else {
      this.dna = new DNA();
    }
    this.pos = createVector(width / 2, height);
    this.vel = createVector();
    this.acc = createVector();
    this.count = 0;
    this.fitness = 0;
    this.completed = false;

    this.applyForce = function(force) {
      this.acc.add(force);
    }

    this.update = function() {
      var d = dist(this.pos.x, this.pos.y, target.x, target.y);
      if (d < 10) {
        this.completed = true;
        this.pos = target.copy();
      }


      this.applyForce(this.dna.genes[count]);
      if (!this.completed) {
        this.vel.add(this.acc);
        this.pos.add(this.vel);
        this.acc.mult(0);
      }
    }

    this.calculateFitness = function() {
      var d = dist(target.x, target.y, this.pos.x, this.pos.y);
      this.fitness = map(d, 0, width, width, 0);
    	if(this.completed){
         this.fitness*=2.5;
         
      }
		}

    this.show = function() {
      push();
      noStroke();
      fill(255, 150);
      translate(this.pos.x, this.pos.y);
      rotate(this.vel.heading());
      rectMode(CENTER);
      rect(0, 0, 25, 5);
      pop();
    }
  }