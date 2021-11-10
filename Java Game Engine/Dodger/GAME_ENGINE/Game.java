package GAME_ENGINE;
import java.awt.Graphics;
import java.awt.Canvas;
import java.awt.Color;
import java.awt.Font;
import java.awt.image.BufferStrategy;
import java.util.Random;
import java.util.Scanner;
/**
 * Write a description of class Game here.
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class Game extends Canvas implements Runnable{
    static Game g;
    public static final float  WIDTH = 1280, HEIGHT = 720;
    private Thread thread;
    public static boolean memes =false;
    private float fps, difficulty = 10;
    Random r = new Random();
    private static boolean running = false;
    private static Handler handler;
    private HUD hud;
    private Spawn spawner;
    private static Menu menu;
    public Window gameWindow;
    public static void main(String[] args){
        g = new Game();
    }

    public enum STATE{
        Menu,
        Help,
        PlayAgain,
        Game
    };
    public static STATE gameState = STATE.Menu;

    public Game(){
        handler = new Handler();//creates the handler for the game
        hud = new HUD();
        spawner = new Spawn(handler, hud);
        menu = new Menu(this,handler);
        this.addKeyListener(new KeyInput(handler,g));
        this.addMouseListener(menu);
        gameWindow = new Window((int)WIDTH,(int)HEIGHT,"SmikaOrigin",this);//creates the games window
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
        g.setColor(Color.black);//set collor
        g.fillRect(0,0,(int)WIDTH,(int)HEIGHT);//draw black box over screen

        handler.render(g);

        if(gameState == STATE.Game){
            hud.render(g);
            g.setColor(Color.white);
            g.setFont(new Font("arial",1,12));
            g.drawString("WASD|^v<>",80,60);
            clamp(KeyInput.special,0,5);
            if(KeyInput.special>0){
                g.drawString("" + KeyInput.special + " SPECIALS READY", 100, 77);
            }
        }else if(gameState == STATE.Menu || gameState == STATE.Help){
            menu.render(g);
        }

        g.drawString("FPS: "+ fps,1,10);
        g.dispose();//clean up
        bs.show();//show
    }

    public static float clamp(float var, float min, float max){
        if(var>=max){
            return var = max;
        }else if(var <= min){
            return var=min;
        }else{
            return var;
        }
    }
    
    public static void close(){
        gameState = STATE.Menu;
        menu = new Menu(g, handler);
        HUD.HEALTH=80;
        HUD.takeTime = true;
        HUD.score = 0;
        HUD.level = 0;
        Spawn.scoreKeep = 0;
    }
    
    public synchronized void start(){
        thread = new Thread(this);
        thread.start();
        running = true;
    }

    public synchronized void stop(){
        try{
            System.out.println("Closing");
            thread.join();
            running = false;
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
