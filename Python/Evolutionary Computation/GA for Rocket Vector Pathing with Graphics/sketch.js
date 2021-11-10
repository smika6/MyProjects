var ppl;
var lifespan = 500;
var lifeP;
var gens;
var count = 0;
var target;
var generations = 0;

var rx = 100;
var ry = 150;
var rw = 200;
var rh = 10;

function setup() {
  createCanvas(400, 300);
  ppl = new Population();
  lifeP = createP();
  gens = createP();
  target = createVector(width / 2, 25);
}

function draw() {
  background(0);
  for(var reps = 0; reps < 10; reps++){
    ppl.run();
    lifeP.html("Sequence:" + count + "/" + lifespan);
    gens.html("Generation: " + generations);
    count++;
    if (count == lifespan) {
      count = 0;
      ppl.evaluate();
      ppl.selection();
      generations++;
      background(255,50);
    }
    fill(	135,206,250);
    rect(rx,ry,rw,rh);
    fill(255,0,0);
    ellipse(target.x, target.y, 20, 20);
	}
}

function Population() {
  this.rockets = [];
  this.popsize = 25;
  this.matingpool = [];

  for (var i = 0; i < this.popsize; i++) {
    this.rockets[i] = new Rocket();
  }

  this.evaluate = function() {
    var maxfit = 0;
    for (var j = 0; j < this.popsize; j++) {
      this.rockets[j].calculateFitness();
      if (this.rockets[j].fitness > maxfit) {
        maxfit = this.rockets[j].fitness;
      }
    }
    createP("Generation " + generations + "'s Max Fitness: " + floor(maxfit));

    for (var i = 0; i < this.popsize; i++) {
      this.rockets[i].fitness /= maxfit;
    }
    this.matingpool = [];
    for (var k = 0; k < this.popsize; k++) {
      var n = this.rockets[k].fitness * 100;
      for (var m = 0; m < n; m++) {
        this.matingpool.push(this.rockets[k]);
      }
    }

  }

  this.selection = function() {
    var newRockets = [];
    for (var i = 0; i < this.rockets.length; i++) {
      var parentA = random(this.matingpool).dna;
      var parentB = random(this.matingpool).dna;
      var child = parentA.crossover(parentB);
      child.mutation();
      newRockets[i] = new Rocket(child);
    }
    this.rockets = newRockets;
  }

  this.run = function() {
    for (var j = 0; j < this.popsize; j++) {
      this.rockets[j].update();
      this.rockets[j].show();
    }
  }
  
  
  
  

  function DNA(genes) {
    if (genes) {
      this.genes = genes;
    } else {
      this.genes = [];
      for (var i = 0; i < lifespan; i++) {
        this.genes[i] = p5.Vector.random2D();
        this.genes[i].setMag(0.1);
      }
    }

    this.crossover = function(partner) {
      var newgenes = [];
      var mid = floor(random(this.genes.length));
      for (var i = 0; i < this.genes.length; i++) {
        if (i > mid) {
          newgenes[i] = this.genes[i];
        } else {
          newgenes[i] = partner.genes[i];
        }
      }
      return new DNA(newgenes);
    }

    this.mutation = function(){
      for(var i = 0; i < this.genes.length; i++){
      	if(random(1) < 0.01){        
           this.genes[i] = p5.Vector.random2D();
           this.genes[i].setMag(0.1);
        }
      }
      
      
      
    }

  }

  
  
  
  
  
  function Rocket(dna) {
    if (dna) {
      this.dna = dna;
    } else {
      this.dna = new DNA();
    }
    this.pos = createVector(width / 2, height-10);
    this.vel = createVector();
    this.acc = createVector();
    this.count = 0;
    this.fitness = 0;
    this.completed = false;
    this.crashed = false;

    this.applyForce = function(force) {
      this.acc.add(force);
    }

    this.update = function() {
      var d = dist(this.pos.x, this.pos.y, target.x, target.y);
      if (d < 10) {
        this.completed = true;
        this.pos = target.copy();
      }
      
      if(this.pos.x > rx && this.pos.x < rx+rw && this.pos.y > ry && this.pos.y < ry + rh){
         this.crashed = true;
      }
      
      if(this.pos.x < 0 || this.pos.x > width){
        this.crashed = true;
      }
      if(this.pos.y < 0 || this.pos.y > height){
        this.crashed = true;
      }


      this.applyForce(this.dna.genes[count]);
      if (!this.completed && !this.crashed) {
        this.vel.add(this.acc);
        this.pos.add(this.vel);
        this.acc.mult(0);
      }
    }

    this.calculateFitness = function() {
      var d = dist(target.x, target.y, this.pos.x, this.pos.y);
      this.fitness = map(d, 0, width, width, 0);
      if (this.completed) {
        this.fitness *= 2.5;
      }else if (d < 25) {
        this.fitness = 500;
      }
      if(this.crashed){
        this.fitness = 1;
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

}