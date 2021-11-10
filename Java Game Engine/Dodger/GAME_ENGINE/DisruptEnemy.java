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
public class DisruptEnemy extends GameObject{
    Handler handler;
    public DisruptEnemy(float x, float y, ID id, Handler handler){
        super(x,y,id);
        this.handler = handler;
        velX=-5;
        velY=-5;
    }

    public void tick(){
        x+=velX;
        y+=velY;
        if(y <= 0 || y >= Game.HEIGHT - 45){
            velY *=-1;
        }
        if(x <= 0 || x >= Game.WIDTH - 25){
            velX *=-1;
        }
        handler.addObject(new Trail(x,y,ID.Trail,20,20,Color.pink,0.06f,handler));
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,20,20);   
    }

    public void render(Graphics g){
        g.setColor(Color.pink);
        g.fillRect((int)x,(int)y,20,20);
    }

}
