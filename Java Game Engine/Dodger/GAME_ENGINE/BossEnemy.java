package GAME_ENGINE;
import java.awt.Graphics;
import java.awt.Color;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;
import java.util.Random;
import java.io.IOException;
/**
 * comes from top, scrolls and fires enemies
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class BossEnemy extends GameObject{
    Handler handler;
    private int timer = 15;
    Random r = new Random();
    private int timer2 = 100;
    boolean left =false, used = false;
    public BossEnemy(float x, float y, ID id, Handler handler, boolean left){
        super(x,y,id);
        this.handler = handler;
        velX=0;
        velY=6;
        this.left = left;
    }

    public void tick(){
        x+=velX;
        y+=velY;
        if(timer<=0){
            velY=0;
        }else{
            timer--;
        }

        if(timer<=0){
            timer2--;
        }
        if(timer2<=0){
            if(velX==0 && !left){
                velX=2;
            }
            if(left && !used){
                velX=-2;
                used=true;
            }
            int spawn = r.nextInt(10);
            if(spawn==7){
                handler.addObject(new BossProjEnemy((int)x+35,(int)y+35, ID.Enemy, handler));
            }
        }
        if(x<=0 || x>=Game.WIDTH -100){
            velX*=-1;
        }
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,90,90);   
    }

    public void render(Graphics g){
        g.setColor(Color.red);
        g.fillRect((int)x,(int)y,90,90);
    }

}
