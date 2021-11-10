 
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.Graphics;
import java.awt.Color;
import java.util.Random;
import java.awt.Font;

/**
 * intro to program menu for user to start with and mouse input
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class Menu extends MouseAdapter{
    private Game game;
    private Handler handler;
    Random r = new Random();
    public Menu(Game game, Handler handler){
        this.game=game;
        this.handler=handler;
        handler.object.clear();
    }

    public void mousePressed(MouseEvent e){
        int mx = e.getX();
        int my = e.getY();
        if(game.getState() == STATE.Menu){
            if(mouseOver(mx,my,540,300,250,80)){//play
                game.setState(STATE.Game);
                HUD.startTime = System.nanoTime();
                handler.clearObjects();
            }

            if(mouseOver(mx,my,540,500,250,80)){//quit
                System.exit(1);
            }

            if(mouseOver(mx,my,540,400,250,80)){//help
            	game.setState(STATE.Help);
            }
        }else if(game.getState() == STATE.Help){
            if(mouseOver(mx,my,540,500,250,80)){//back
            	game.setState(STATE.Menu);
            }
        }
    }

    public void mouseReleased(MouseEvent e){}

    private boolean mouseOver(int mx, int my, int x, int y, int width, int height){
        if( mx>x && mx<x+width){
            if( my>y && my<y+height){
                return true;
            }
        }
        return false;
    }

    public void tick(){}

    public void render(Graphics g){
        if(game.getState() == STATE.Menu){
            g.setColor(Color.white);
            Font fnt = new Font("arial", 1, 50);
            Font fnt2 = new Font("arial", 1, 30);
            g.setFont(fnt);
            g.drawString("SmikaZombieDefense",500,240);
            g.setFont(fnt2);
            g.drawString("By Jacob Hopkins 2/1/2019", 500, 280);
            g.drawString("Play",610,350);
            g.drawRect(540,300,250,80);
            g.drawString("Help",610,450);
            g.drawRect(540,400,250,80);
            g.drawString("Quit",610,550);
            g.drawRect(540,500,250,80);
            g.setFont(new Font("arial",1,12));
        }else if(game.getState() == STATE.Help){
            g.setColor(Color.white);
            Font fnt = new Font("arial", 1, 50);
            g.setFont(fnt);
            g.drawString("Help",600,240);
            Font fnt2 = new Font("arial", 1, 30);
            g.setFont(fnt2);
            g.drawString("Alpha version of zombie defense game",300,400);
            g.drawString("Arrow Keys to move",300,450);
            g.drawString("Back",610,550);
            g.drawRect(540,500,250,80);
            g.setFont(new Font("arial",1,12));
        }else if(game.getState() == STATE.PlayAgain){
            g.setColor(Color.white);
            Font fnt = new Font("arial", 1, 50);
            g.setFont(fnt);
            g.drawString("Play Again?",610,550);
            g.drawRect(540,500,250,80);
            g.setFont(new Font("arial",1,12));
        }
    }
}
