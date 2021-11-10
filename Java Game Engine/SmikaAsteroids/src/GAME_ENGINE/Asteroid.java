package GAME_ENGINE;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.Random;

public class Asteroid extends GameObject{
    Handler handler;
    Random r = new Random();
    public Game game;
    public float health;
    public Asteroid(float x, float y, ID id, Handler handler, Game game){
        super(x, y, id);
        this.handler = handler;
        this.game = game;
        this.velX=r.nextInt(5);
        this.velY=r.nextInt(5);
        health = (r.nextInt(75)+50)-25;
    }

    public void collision(){
        GameObject[] trash = new GameObject[1];
        for(int i = 0; i < handler.getObjects().size(); i++){
            GameObject tempObject = handler.getObjects().get(i);
            //check for collision
            if(tempObject.getId() == ID.Bullet) {
            	if(this.getBounds().intersects(tempObject.getBounds())) {
            		trash[0] = tempObject;
            		health-=15;
            	}
            }
            if(health<= 10) {
            	handler.removeObject(this);
            }
            if(x<0 || x > game.WIDTH) {
            	velX*=-1;
            }
            if(y<0 || y > game.HEIGHT) {
            	velY*=-1;
            }
        }
        if(trash!=null){
            handler.removeObject(trash[0]);
        }
    }

    public void tick(){
            x += velX;
            y += velY;
        collision();
    }

    public void render(Graphics g){
        g.setColor(Color.LIGHT_GRAY);
        g.fillOval((int)x,(int)y,Math.round(health),Math.round(health));
        
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,Math.round(health),Math.round(health));
    }

}
