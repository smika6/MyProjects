package GAME_ENGINE;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.AlphaComposite;
import java.awt.Graphics2D;
import java.awt.Color;
/**
 * Write a description of class Trail here.
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class Trail extends GameObject{
    private float alpha = 1;
    private Handler handler;
    private Color color;
    private float width,height;
    private float life;
    public Trail(float x, float y, ID id, float width, float height, Color color, float life, Handler handler){
        super(x,y,id);
        this.handler = handler;
        this.color=color;
        this.width=width;
        this.height=height;
        this.life=life;
    }
    
    public void tick(){
        if(alpha > life){
            alpha-=life-0.001f;
        }else{
            handler.removeObject(this);
        }
    }
    
    public void render(Graphics g){
        Graphics2D g2d = (Graphics2D) g;
        g2d.setComposite(makeTransparent(alpha));
        
        g.setColor(color);
        g.fillRect((int)x,(int)y,(int)width,(int)height);
        
        g2d.setComposite(makeTransparent(1));
    }
    
    private AlphaComposite makeTransparent(float alpha){
        int type = AlphaComposite.SRC_OVER;
        return AlphaComposite.getInstance(type,alpha);
    }
    
    public Rectangle getBounds(){
        return null;
    }
}
