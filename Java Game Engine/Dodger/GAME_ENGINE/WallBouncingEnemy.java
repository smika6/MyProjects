package GAME_ENGINE;
import java.awt.Graphics;
import java.awt.Color;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;
/**
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class WallBouncingEnemy extends GameObject{
    Handler handler;
    public WallBouncingEnemy(float x, float y, ID id, Handler handler){
        super(x,y,id);
        this.handler = handler;
        velX=4;
        velY=4;
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
        handler.addObject(new Trail(x,y,ID.Trail,30,30,Color.lightGray,0.07f,handler));
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,30,30);   
    }

    public void render(Graphics g){
        g.setColor(Color.lightGray);
        g.fillRect((int)x,(int)y,30,30);
    }

}
