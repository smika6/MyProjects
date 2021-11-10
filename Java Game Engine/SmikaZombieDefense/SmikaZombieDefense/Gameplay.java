 
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
    private HUD hud;
    Random r = new Random();
    public int difficulty = 1000;
    public int waves = 0;
    Player player;
    public Gameplay(Handler handler, HUD hud, Game game){
        this.handler = handler;
        this.hud = hud;
        this.game = game;
    }

    public void tick(){
    	for(int i=0;i<handler.object.size();i++){
            if(handler.object.get(i).getId() == ID.Player){
                player = (Player) handler.object.get(i);
            }
        }
    	//put in game stages here
    	if(r.nextInt(difficulty)<10) {
    		spawnZombie(1);
    	}
    }
    
    public void spawnZombie(int x){
        for(int i=0;i<x;i++){
            handler.addObject(new Zombie(r.nextInt((int) game.WIDTH+50)-50,r.nextInt((int)game.HEIGHT+50)-50,ID.Zombie,handler));
	        difficulty--;
	    }
    }
}
