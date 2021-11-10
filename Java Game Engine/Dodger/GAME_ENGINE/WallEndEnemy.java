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
public class WallEndEnemy extends GameObject{
    Handler handler;
    public WallEndEnemy(float x, float y, ID id, Handler handler, int dirX, int dirY){
        super(x,y,id);
        this.handler = handler;
        velX = dirX;
        velY = dirY;
    }

    public void tick(){
        x+=velX;
        y+=velY;
        if(y <= 0 || y >= Game.HEIGHT - 55){
            handler.removeObject(this);
        }
        if(x <= 0 || x >= Game.WIDTH - 35){
            handler.removeObject(this);
        }
        handler.addObject(new Trail(x,y,ID.Trail,30,30,Color.lightGray,0.1f,handler));
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,30,30);   
    }

    public void render(Graphics g){
        g.setColor(Color.lightGray);
        g.fillRect((int)x,(int)y,30,30);
    }

}
