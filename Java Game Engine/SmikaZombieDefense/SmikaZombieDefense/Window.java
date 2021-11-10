 
import java.awt.Canvas;
import java.awt.Dimension;
import javax.swing.JFrame;
/**
 * creates a prototype game window
 * that can display images, pixels, and game element objects
 *
 * @author Jacob Hopkins
 * @version v1.0
 * @Date 6/10/2018
 */
public class Window extends Canvas{
    private static final long serialVersionUID = -2631997420717L;
    public Window(int width, int height, String title, Game game){//my unique window
        JFrame frame = new JFrame(title);//window for the game
        
        frame.setPreferredSize(new Dimension(width,height));
        frame.setMaximumSize(new Dimension(width,height));
        frame.setMinimumSize(new Dimension(width,height));
        
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//top right X closes program
        frame.setResizable(false);//cannot resize my window
        frame.setLocationRelativeTo(null);//spawns screen in center not top left
        frame.add(game);//adds me game to the window
        frame.setVisible(true);//makes my window visible to user
        
        game.start();//starts the game
    }
}