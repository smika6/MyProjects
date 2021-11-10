package GAME_ENGINE;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.Random;

public class Bullet extends GameObject{
	private Handler handler;
    private Random r = new Random();
    private Player player;
    public Bullet(float x, float y, ID id, Handler handler){
        super(x, y, id);
        this.handler = handler;
        for(int i=0;i<handler.object.size();i++){
            if(handler.object.get(i).getId() == ID.Player){
                player = (Player)handler.object.get(i);
            }
        }
        if(player.velX != 0 && player.velY != 0) {
        	velX = 2*player.velX;
        	velY = 2*player.velY;
        }else if(player.facing == DIRECTION.EAST) {
        	velX = 9;
        }else if(player.facing == DIRECTION.WEST) {
        	velX = -9;
        }else if(player.facing == DIRECTION.SOUTH) {
        	velY = 9;
        }else if(player.facing == DIRECTION.NORTH) {
        	velY = -9;
        }
    }
    
    public void collision(){
        GameObject[] trash = new GameObject[1];
        for(int i = 0; i < handler.object.size(); i++){
            GameObject tempObject = handler.object.get(i);
            //check for collision
            if(tempObject.getId() == ID.Zombie) {
            	if(getBounds().intersects(tempObject.getBounds())) {
            		trash[0]=this;
            		HUD.HEALTH+=2;
            	}
            }
            if(x<0 || x>Game.WIDTH || y>Game.HEIGHT || y < 0) {
            	trash[0] = this;
            }
        }
        if(trash!=null){
            handler.removeObject(trash[0]);
        }
    }
    
    public void tick(){
    	
        x += velX;
        y += velY;
    }
    
    public void render(Graphics g){
        g.setColor(Color.white);
        g.fillRect((int)x,(int)y,15,15);
    }
    
    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,15,15);
    }
}
