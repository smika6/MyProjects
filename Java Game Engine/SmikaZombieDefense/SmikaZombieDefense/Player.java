 
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
    DIRECTION facing;
    int kills;
    public Player(float x, float y, ID id, Handler handler){
        super(x, y, id);
        this.handler = handler;
    }

    public void collision(){
        GameObject[] trash = new GameObject[1];
        for(int i = 0; i < handler.object.size(); i++){
            GameObject tempObject = handler.object.get(i);
            //check for collision
            if(tempObject.getId() == ID.Zombie ) {
            	if(getBounds().intersects(tempObject.getBounds())){
                    HUD.HEALTH-=1;
                }
            }
        }
        if(trash!=null){
            handler.removeObject(trash[0]);
        }
    }

    public void tick(){
        if(HUD.HEALTH>0){
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
        y = AuxFunctions.clamp(y, 0, Game.HEIGHT - 55);
        x = AuxFunctions.clamp(x, 0, Game.WIDTH - 30);
        collision();
    }

    public void render(Graphics g){
        g.setColor(Color.blue);
        g.fillRect((int)x,(int)y,25,25);
        g.setColor(Color.GRAY);
        if(facing == DIRECTION.EAST) {
        	g.fillRect((int)x+25, (int)y+8,20,10);
        }else if(facing == DIRECTION.WEST) {
        	g.fillRect((int)x-20, (int)y+8,20,10);
        }else if(facing == DIRECTION.SOUTH) {
        	g.fillRect((int)x+8, (int)y+25,10,20);
        }else if(facing == DIRECTION.NORTH) {
        	g.fillRect((int)x+8, (int)y-20,10,20);
        }
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,25,25);
    }

}
