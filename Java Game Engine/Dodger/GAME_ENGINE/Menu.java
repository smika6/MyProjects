package GAME_ENGINE;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.Graphics;
import java.awt.Color;
import java.util.Random;
import java.awt.Font;
import GAME_ENGINE.Game.STATE;
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
        handler.addObject(new popUpEnemy((float)r.nextInt((int)(Game.WIDTH-50)),(float)r.nextInt((int)(Game.HEIGHT-50)),ID.Enemy, handler));
        handler.addObject(new WallBouncingEnemy((float)r.nextInt((int)(Game.WIDTH-50)),(float)r.nextInt((int)(Game.HEIGHT-50)),ID.Enemy, handler));
        handler.addObject(new DisruptEnemy((float)r.nextInt((int)(Game.WIDTH-50)),(float)r.nextInt((int)(Game.HEIGHT-50)),ID.DisruptEnemy, handler));
        handler.addObject(new FastEnemy((float)r.nextInt((int)(Game.WIDTH-50)),(float)r.nextInt((int)(Game.HEIGHT-50)),ID.Enemy, handler));
    }

    public void mousePressed(MouseEvent e){
        int mx = e.getX();
        int my = e.getY();
        if(Game.gameState == STATE.Menu){
            if(mouseOver(mx,my,540,300,250,80)){//play
                game.gameState = STATE.Game;
                HUD.startTime = System.nanoTime();
                handler.clearObjects();
                handler.addObject(new DisruptEnemy((float)r.nextInt((int)(Game.WIDTH-50)),(float)r.nextInt((int)(Game.HEIGHT-50)),ID.DisruptEnemy, handler));
                handler.addObject(new HealthPod((float)r.nextInt((int)(Game.WIDTH-150)),(float)r.nextInt((int)(Game.HEIGHT-150)),ID.HealthPod, handler));
            }

            if(mouseOver(mx,my,540,500,250,80)){//qqquit
                System.exit(1);
            }

            if(mouseOver(mx,my,540,400,250,80)){//help
                game.gameState = STATE.Help;
            }
        }else if(Game.gameState == STATE.Help){
            if(mouseOver(mx,my,540,500,250,80)){//back
                game.gameState = STATE.Menu;
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
        if(Game.gameState == STATE.Menu){
            g.setColor(Color.white);
            Font fnt = new Font("arial", 1, 50);
            Font fnt2 = new Font("arial", 1, 30);
            g.setFont(fnt);
            g.drawString("Dodger",600,240);
            g.setFont(fnt2);
            g.drawString("By Jacob Hopkins 6/11/2018", 600, 280);
            g.drawString("Play",610,350);
            g.drawRect(540,300,250,80);
            g.drawString("Help",610,450);
            g.drawRect(540,400,250,80);
            g.drawString("Quit",610,550);
            g.drawRect(540,500,250,80);
            g.setFont(new Font("arial",1,12));
        }else if(Game.gameState == STATE.Help){
            g.setColor(Color.white);
            Font fnt = new Font("arial", 1, 50);
            g.setFont(fnt);
            g.drawString("Help",600,240);
            Font fnt2 = new Font("arial", 1, 30);
            g.setFont(fnt2);
            g.drawString("Dodge Enemies, win by highscore, lose at 0hp",300,400);
            g.drawString("ArrowKeys / wasd to move, new wave every 1000 score",300,450);
            g.drawString("Back",610,550);
            g.drawRect(540,500,250,80);
            g.setFont(new Font("arial",1,12));
        }else if(Game.gameState == STATE.PlayAgain){
            g.setColor(Color.white);
            Font fnt = new Font("arial", 1, 50);
            g.setFont(fnt);
            g.drawString("Play Again?",610,550);
            g.drawRect(540,500,250,80);
            g.setFont(new Font("arial",1,12));
        }
    }
}
