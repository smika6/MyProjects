package GAME_ENGINE;
import java.awt.Graphics;
import java.awt.Color;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.util.Random;
import java.io.File;
import java.io.IOException;
/**
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class popUpEnemy extends GameObject{
    Handler handler;
    int count=0;
    Random r = new Random();
    public popUpEnemy(float x, float y, ID id, Handler handler){
        super(x,y,id);
        this.handler = handler;
    }

    public void tick(){
        count++;
        if(r.nextInt(50)==7){
            pulse();
        }
        if(count>=200){
            handler.removeObject(this);
        }

    }

    public void pulse(){
        int speed = 3;
        handler.addObject(new WallEndEnemy(x,y,ID.Enemy, handler, 0, speed));
        handler.addObject(new WallEndEnemy(x,y,ID.Enemy, handler, 0, -speed));
        handler.addObject(new WallEndEnemy(x,y,ID.Enemy, handler, speed, 0));
        handler.addObject(new WallEndEnemy(x,y,ID.Enemy, handler, -speed, 0));
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,30,30);   
    }

    public void render(Graphics g){
        g.setColor(Color.darkGray);
        g.fillRect((int)x,(int)y,30,30);
    }

}
