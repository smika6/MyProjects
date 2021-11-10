package GAME_ENGINE;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.Random;

/**
 * @author Jacob
 * @version v1.0
 */
public class Zombie extends GameObject{
	Handler handler;
    Random r = new Random();
    private Player player;
    public Zombie(float x, float y, ID id, Handler handler){
        super(x, y, id);
        this.handler = handler;
        for(int i=0;i<handler.object.size();i++){
            if(handler.object.get(i).getId() == ID.Player){
                player = (Player) handler.object.get(i);
            }
        }
    }
    
    public void collision(){
        GameObject[] trash = new GameObject[1];
        for(int i = 0; i < handler.object.size(); i++){
            GameObject tempObject = handler.object.get(i);
            //check for collision
            if(tempObject.getId() == ID.Bullet) {
            	if(getBounds().intersects(tempObject.getBounds())) {
            		trash[0]=this;
            		HUD.HEALTH++;
            		HUD.kills++;
            	}
            	if(tempObject.x<0 || tempObject.x>Game.WIDTH || tempObject.y>Game.HEIGHT || tempObject.y < 0) {
                	trash[0] = tempObject;
                }
            }
            if(trash!=null){
                handler.removeObject(trash[0]);
                //handler.removeObject(this);
            }
        }
    }
    
    public void tick(){
        x += velX;
        y += velY;
        float diffX = x - player.getX() - 7;
        float diffY = y - player.getY() - 7;
        float distance = (float)Math.sqrt((x-player.getX())*(x-player.getX()) + (y-player.getY())*(y-player.getY()));
        velX = (float) ((-1.0/distance) * diffX); 
        velY = (float) ((-1.0/distance) * diffY);
        
        y = AuxFunctions.clamp(y, 0, Game.HEIGHT - 50);
        x = AuxFunctions.clamp(x, -500, Game.WIDTH - 30);
        collision();
    }
    
    public void render(Graphics g){
        g.setColor(Color.red);
        g.fillRect((int)x,(int)y,25,25);
    }
    
    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,25,25);
    }
}
