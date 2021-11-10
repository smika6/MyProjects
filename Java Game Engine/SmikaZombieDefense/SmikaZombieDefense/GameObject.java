 
import java.awt.Graphics;
import java.awt.Rectangle;
/**
 * an generic abstract object parent object for game elements
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public abstract class GameObject{
    protected float x, y;
    protected ID id;
    protected float velX, velY;
    
    public GameObject(float x, float y, ID id){
        this.x = x;
        this.y = y;
        this.id = id;
    }
    
    public abstract void tick();
    
    public abstract void render(Graphics g);
    
    public abstract Rectangle getBounds();
    
    public void setX(float x){
        this.x = x;
    }
    public void setY(float y){
        this.y = y;
    }
    public float getX(){
        return x;
    }
    public float getY(){
        return y;
    }
    public void setId(ID id){
        this.id = id;
    }
    public ID getId(){
        return id;
    }
    public void setVelX(float vX){
        this.velX = vX;
    }
    public void setVelY(float vY){
        this.velY = vY;
    }
    public float getVelX(){
        return velX;
    }
    public float getVelY(){
        return velY;
    }
}
