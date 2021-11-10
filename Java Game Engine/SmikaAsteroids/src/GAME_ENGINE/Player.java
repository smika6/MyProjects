package GAME_ENGINE;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.Random;
/**
 * users interface to win the game
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class Player extends GameObject{
    Handler handler;
    Random r = new Random();
    public Game game;
    DIRECTION facing;
    public Player(float x, float y, ID id, Game game){
        super(x, y, id);
        this.handler = game.getHandler();
        this.game = game;
    }

    public void collision(){
        GameObject[] trash = new GameObject[1];
        for(int i = 0; i < handler.getObjects().size(); i++){
            GameObject tempObject = handler.getObjects().get(i);
            //check for collision
            if(tempObject.getId() == ID.Asteroid) {
            	if(this.getBounds().intersects(tempObject.getBounds())) {
            		trash[0] = tempObject;
            		HUD.add2Health(-20);
            	}
            }
        }
        if(trash!=null){
            handler.removeObject(trash[0]);
        }
    }

    public void tick(){
        if(HUD.getHealth()>0){
            x += velX;
            y += velY;
            if(velX>0) {
            	facing = DIRECTION.EAST;
            }
            if(velX<0) {
            	facing = DIRECTION.WEST;
            }
            if(velY>0) {
            	facing = DIRECTION.SOUTH;
            }
            if(velY<0) {
            	facing = DIRECTION.NORTH;
            }
        }
        y = AuxFunctions.clamp(y, 0, Game.HEIGHT-25);
        x = AuxFunctions.clamp(x, 0, Game.WIDTH-25);
        collision();
    }

    public void render(Graphics g){
        g.setColor(Color.WHITE);
        g.fillOval((int)x,(int)y,25,25);
        
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,25,25);
    }

}
