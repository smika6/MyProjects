package GAME_ENGINE;
import java.awt.Graphics;
import java.awt.Color;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;
import java.util.Random;
/**
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class BossProjEnemy extends GameObject{
    Handler handler;
    Random r = new Random();
    public BossProjEnemy(float x, float y, ID id, Handler handler){
        super(x,y,id);
        this.handler = handler;

        velX=(r.nextInt(5 - -5)+-5);
        velY=5;
    }

    public void tick(){
        x+=velX;
        y+=velY;
        if(y >= Game.HEIGHT - 55){
            handler.removeObject(this);
        }
        if(x <= 0 || x >= Game.WIDTH - 35){
            velX *=-1;
        }
        handler.addObject(new Trail(x,y,ID.Trail,30,30,Color.magenta,0.07f,handler));
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,30,30);   
    }

    public void render(Graphics g){
        g.setColor(Color.magenta);
        g.fillRect((int)x,(int)y,30,30);
    }

}
