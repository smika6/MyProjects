 
import java.awt.Graphics;
import java.awt.Canvas;
import java.awt.Color;
import java.awt.image.BufferStrategy;
import java.util.Random;
/**
 * Write a description of class Game here.
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
@SuppressWarnings("serial")
public class Game extends Canvas implements Runnable{
	private static Game g;
    public static final float  WIDTH = 1280, HEIGHT = 720;
    private Thread thread;
    private float fps;
    private static boolean running = false;
    private static Handler handler;
    private HUD hud;
    private Gameplay spawner;
    private static Menu menu;
    private Window gameWindow;
    private static STATE gameState = STATE.Menu;
    KeyInput keyInput;
    public static void main(String[] args){
        g = new Game();
    }

    public Game(){
        handler = new Handler();//creates the handler for the game
        hud = new HUD(g);
        spawner = new Gameplay(handler, hud, g);
        menu = new Menu(this,handler);
        keyInput = new KeyInput(handler,g);
        this.addKeyListener(keyInput);
        this.addMouseListener(menu);
        gameWindow = new Window((int)WIDTH,(int)HEIGHT,"SmikaZombieDefense",this);//creates the games window
    }

    public void run(){
        long lastTime = System.nanoTime();
        double tickCount = 60.0;
        double ns = 1000000000 / tickCount;
        double delta = 0;
        long timer = System.currentTimeMillis();
        int frames = 0;
        while(running){
            long now = System.nanoTime();
            delta += (now-lastTime)/ns;
            lastTime = now;
            while(delta>=1){
                tick();
                delta--;
            }
            if(running)
                render();
            frames++;
            if(System.currentTimeMillis() - timer > 1000){
                timer+=1000;
                //System.out.println("FPS: " + frames);
                fps = frames;
                frames = 0;
            }
        }
        stop();
    }

    private void tick(){
        handler.tick();
        if(gameState == STATE.Game){
            hud.tick();
            spawner.tick();
        }else if(gameState == STATE.Menu){
            menu.tick();
        }
    }
    

    private void render(){
        BufferStrategy bs = this.getBufferStrategy();
        if(bs == null){
            this.createBufferStrategy(3);
            return;
        }

        Graphics g = bs.getDrawGraphics();
        g.setColor(Color.black);//set color
        g.fillRect(0,0,(int)WIDTH,(int)HEIGHT);//draw black box over screen

        handler.render(g);

        if(gameState == STATE.Game){
            hud.render(g);
        }else if(gameState == STATE.Menu || gameState == STATE.Help){
            menu.render(g);
        }

        g.drawString("FPS: "+ fps,1,10);
        g.dispose();//clean up
        bs.show();//show
    }
    
    public static STATE getState() {
    	return gameState;
    }
    
    public static void setState(STATE state) {
    	gameState = state;
    }
    
    public static void close(){
        gameState = STATE.Menu;
        menu = new Menu(g, handler);
        HUD.HEALTH=80;
        HUD.takeTime = true;
    }
    
    public synchronized void start(){
        thread = new Thread(this);
        thread.start();
        running = true;
    }

    public synchronized void stop(){
        try{
            thread.join();
            running = false;
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
