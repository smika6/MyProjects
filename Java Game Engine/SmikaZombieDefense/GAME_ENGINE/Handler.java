package GAME_ENGINE;
import java.util.LinkedList;
import java.awt.Graphics;
/**
 * maintain/update&render objects
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class Handler{
    LinkedList<GameObject> object = new LinkedList<GameObject>();
    public void tick(){
        for(int i = 0;i < object.size();i++){
            GameObject tempObject = object.get(i);
            tempObject.tick();
        }
        System.out.println(object.size());
    }
    
    public void render(Graphics g){
        for(int i = object.size();i > 0;i--){
            GameObject tempObject = object.get(i-1);
            tempObject.render(g);
        }
    }
    
    public void addObject(GameObject object){
        this.object.add(object);
    }
    
    public void addFirst(GameObject object){
        this.object.addFirst(object);
    }
    
    public void removeObject(GameObject object){
        this.object.remove(object);
    }
    
    public void removeObject(int index){
        this.object.remove(index);
    }
    
    public void clearObjects(){
        int x = (int)Game.WIDTH/2, y = (int)Game.HEIGHT/2;
        for(GameObject temp:object){
            if(temp.getId() == ID.Player){
                x=(int)temp.getX();
                y=(int)temp.getY();
            }
        }
        this.object.clear();
        this.addObject(new Player(x,y,ID.Player, this));
    }
    
    public int lastIndexOf(GameObject object){
        return this.object.indexOf(object);
    }
    
    public GameObject getObject(int index){
        return object.get(index);
    }
    
    public GameObject removeLast(){
        return object.removeLast();
    }
}
