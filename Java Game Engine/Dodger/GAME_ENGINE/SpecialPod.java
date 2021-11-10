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
public class SpecialPod extends GameObject{
    Handler handler;
    public int life = 500;
    public SpecialPod(float x, float y, ID id, Handler handler){
        super(x,y,id);
        this.handler = handler;
    }

    public void tick(){
        life--;
        if(life==0){
            handler.removeObject(this);
        }
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,30,30);   
    }

    public void render(Graphics g){
        g.setColor(Color.yellow);
        g.fillRect((int)x,(int)y,30,30);
    }

}
