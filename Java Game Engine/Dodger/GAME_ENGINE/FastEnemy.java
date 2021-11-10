package GAME_ENGINE;
import java.awt.Graphics;
import java.awt.Color;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;
/**
 *bounces across screen quickly
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class FastEnemy extends GameObject{
    Handler handler;
    public FastEnemy(float x, float y, ID id, Handler handler){
        super(x,y,id);
        this.handler = handler;
        velX=6;
        velY=6;
    }

    public void tick(){
        x+=velX;
        y+=velY;
        if(y <= 0 || y >= Game.HEIGHT - 55){
            velY *=-1;
        }
        if(x <= 0 || x >= Game.WIDTH - 35){
            velX *=-1;
        }
        handler.addObject(new Trail(x,y,ID.Trail,30,30,Color.gray,0.07f,handler));
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,30,30);   
    }

    public void render(Graphics g){
        g.setColor(Color.gray);
        g.fillRect((int)x,(int)y,30,30);
    }

}
