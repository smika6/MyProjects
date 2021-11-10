package GAME_ENGINE;
import java.awt.Graphics;
import java.awt.Color;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;
/**
 *go towards player
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class TrackingEnemy extends GameObject{
    Handler handler;
    private GameObject player;
    public TrackingEnemy(float x, float y, ID id, Handler handler){
        super(x,y,id);
        this.handler = handler;
        for(int i=0;i<handler.object.size();i++){
            if(handler.object.get(i).getId() == ID.Player){
                player = handler.object.get(i);
            }
        }
    }

    public void tick(){
        x+=velX;
        y+=velY;

        float diffX = x - player.getX() - 7;
        float diffY = y - player.getY() - 7;
        float distance = (float)Math.sqrt((x-player.getX())*(x-player.getX()) + (y-player.getY())*(y-player.getY()));

        velX = (float) ((-1.0/distance) * diffX); 
        velY = (float) ((-1.0/distance) * diffY);

        if(y <= 0 || y >= Game.HEIGHT - 70){
            velY *=-1;
        }
        if(x <= 0 || x >= Game.WIDTH - 55){
            velX *=-1;
        }
        handler.addObject(new Trail(x,y,ID.Trail,50,50,Color.gray,0.1f,handler));
    }

    public Rectangle getBounds(){
        return new Rectangle((int)x,(int)y,50,50);   
    }

    public void render(Graphics g){
        String workingDir = System.getProperty("user.dir");
        workingDir+="\\GAME_ENGINE\\zucc.jpg";
        //System.out.println(workingDir);
        if(Game.memes==true){
            try{
                BufferedImage image = ImageIO.read(new File(workingDir));
                g.drawImage(image,(int)x,(int)y,null);
            }catch(Exception e){e.printStackTrace();}
        }else{
            g.setColor(Color.gray);
            g.fillRect((int)x,(int)y,50,50);
        }
    }

}
