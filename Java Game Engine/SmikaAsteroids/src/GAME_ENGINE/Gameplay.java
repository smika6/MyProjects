package GAME_ENGINE;
import java.util.*;
/**
 * Write a description of class Spawn here.
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class Gameplay{
	private Game game;
    private Handler handler;
    Random r = new Random();
    public int difficulty = 1000;
    public Gameplay(Game game){
        this.handler = game.getHandler();
        this.game = game;
    }

    public void tick(){
    	//put in game stages here
    	if(r.nextInt(difficulty)<10) {
    		spawnAsteroid(1);
    	}
    }
    
    public void spawnAsteroid(int x){
        for(int i=0;i<x;i++){
            handler.addObject(new Asteroid(r.nextInt((int) game.WIDTH+50)-50,r.nextInt((int)game.HEIGHT+50)-50,ID.Asteroid,handler, game));
	        difficulty--;
	    }
    }
}
