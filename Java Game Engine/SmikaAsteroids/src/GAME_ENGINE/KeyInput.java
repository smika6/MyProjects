package GAME_ENGINE;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
/**
 * keyboard input from user
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class KeyInput extends KeyAdapter{
    private Handler handler;
    private Game g;
    private boolean[] keyDown = new boolean[4];
    public static int special = 0;
    private Player player;
    public KeyInput(Handler handler, Game g){
        this.handler = handler;
        this.g=g;
        for(boolean b : keyDown){
            b=false;
        }
    }

    public void keyPressed(KeyEvent e){
    	for(int i=0;i<handler.getObjects().size();i++){
            if(handler.getObjects().get(i).getId() == ID.Player){
                player = (Player) handler.getObjects().get(i);
            }
        }
        int key = e.getKeyCode();
        for(int i=0;i<handler.getObjects().size();i++){
            GameObject tempObject = handler.getObjects().get(i);

            if(tempObject.getId() == ID.Player){
                if(HUD.getHealth()>0){
                    if(key == KeyEvent.VK_W || key == KeyEvent.VK_UP ){tempObject.setVelY(-5); keyDown[0]=true;}
                    if(key == KeyEvent.VK_A || key == KeyEvent.VK_LEFT ){tempObject.setVelX(-5); keyDown[2]=true;}
                    if(key == KeyEvent.VK_S || key == KeyEvent.VK_DOWN ){tempObject.setVelY(5); keyDown[1]=true;}
                    if(key == KeyEvent.VK_D || key == KeyEvent.VK_RIGHT){tempObject.setVelX(5); keyDown[3]=true;}
                    if(key==KeyEvent.VK_SPACE) {
                    	handler.addObject(new Bullet(player.x,player.y,ID.Bullet,handler));
                    }
                }
                if(key == KeyEvent.VK_M){
                    g.close();
                }
                if(keyDown[0] && keyDown[2]){
                    tempObject.setVelY(-4.2f);
                    tempObject.setVelX(-4.2f);
                }
                if(keyDown[0] && keyDown[3]){
                    tempObject.setVelY(-4.2f);
                    tempObject.setVelX(4.2f);
                }
                if(keyDown[1] && keyDown[2]){
                    tempObject.setVelY(4.2f);
                    tempObject.setVelX(-4.2f);
                }
                if(keyDown[1] && keyDown[3]){
                    tempObject.setVelY(4.2f);
                    tempObject.setVelX(4.2f);
                }
            }
        }
        if(key == KeyEvent.VK_ESCAPE){System.exit(1);}
    }

    public void keyReleased(KeyEvent e){
        int key = e.getKeyCode();
        for(int i=0;i<handler.getObjects().size();i++){
            GameObject tempObject = handler.getObjects().get(i);
            if(tempObject.getId() == ID.Player){
                if(key == KeyEvent.VK_W || key == KeyEvent.VK_UP ){keyDown[0]=false;}
                if(key == KeyEvent.VK_A || key == KeyEvent.VK_LEFT ){keyDown[2]=false;}
                if(key == KeyEvent.VK_S || key == KeyEvent.VK_DOWN ){keyDown[1]=false;}
                if(key == KeyEvent.VK_D || key == KeyEvent.VK_RIGHT){keyDown[3]=false;}
                if(!keyDown[0] && !keyDown[1]){tempObject.setVelY(0);}
                if(!keyDown[2] && !keyDown[3]){tempObject.setVelX(0);}
            }
        }
    }

}
