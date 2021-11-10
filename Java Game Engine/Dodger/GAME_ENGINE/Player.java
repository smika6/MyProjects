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
    public Player(float x, float y, ID id, Handler handler){
        super(x, y, id);
        this.handler = handler;
    }

    public void collision(){
        GameObject[] trash = new GameObject[1];
        for(int i = 0; i < handler.object.size(); i++){
            GameObject tempObject = handler.object.get(i);

            if(tempObject.getId() == ID.Enemy){
                if(getBounds().intersects(tempObject.getBounds())){
                    HUD.HEALTH-=2;
                }
            }else if(tempObject.getId() == ID.DisruptEnemy){
                if(getBounds().intersects(tempObject.getBounds())){
                    this.setVelX(r.nextInt(5)+1);
                    this.setVelY(r.nextInt(5)+1);
                }
            }else if(tempObject.getId() == ID.TrackingEnemy){
                if(getBounds().intersects(tempObject.getBounds())){
                    this.setVelX(2*this.getVelX()*-1);
                    this.setVelY(2*this.getVelY()*-1);
                    HUD.HEALTH-=1;
                }
            }else if(tempObject.getId() == ID.Boss){
                if(getBounds().intersects(tempObject.getBounds())){
                    HUD.HEALTH-=5;
                }
            }else if(tempObject.getId() == ID.HealthPod){
                if(getBounds().intersects(tempObject.getBounds())){
                    HUD.HEALTH=100;
                    trash[0]=tempObject;
                }
            }else if(tempObject.getId() == ID.SpecialPod){
                if(getBounds().intersects(tempObject.getBounds())){
                    KeyInput.special++;
                    trash[0]=tempObject;
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
        }
        y = Game.clamp(y, 0, Game.HEIGHT - 50);
        x = Game.clamp(x, 0, Game.WIDTH - 30);

        handler.addObject(new Trail(x,y,ID.Trail,25,25,Color.blue,0.07f,handler));
        collision();
    }

    public void render(Graphics g){
        g.setColor(Color.blue);
        g.fillRect((int)x,(int)y,25,25);
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,25,25);
    }

}
