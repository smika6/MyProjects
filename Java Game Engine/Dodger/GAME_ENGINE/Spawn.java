package GAME_ENGINE;
import java.util.*;
/**
 * Write a description of class Spawn here.
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class Spawn{
    private Handler handler;
    private HUD hud;
    Random r = new Random();
    private boolean minnions = false;
    public static int scoreKeep = 0;
    public Spawn(Handler handler, HUD hud){
        this.handler = handler;
        this.hud = hud;
    }

    public void tick(){
        scoreKeep++;
        if(r.nextInt(1000)==1){
            popUpEnemy(1);
        }
        if(scoreKeep>=1000){
            KeyInput.special++;
            scoreKeep = 0;
            hud.setLevel(hud.getLevel()+1);

            if(hud.getLevel()==1){//3
                handler.clearObjects();
                if(scoreKeep%1050==0){
                    popUpEnemy(1);
                    wallBounceEnemy(3);
                }
            }

            if(hud.getLevel()==2){//8
                wallBounceEnemy(5);
            }

            if(hud.getLevel()==3){//12
                disruptEnemy(4);
            }

            if(hud.getLevel()==4){//17
                handler.clearObjects();
                if(scoreKeep%1050==0){
                    wallBounceEnemy(5);
                    disruptEnemy(5);
                    trackingEnemy(2);
                    fastEnemy(5);
                }
            }

            if(hud.getLevel()==4){
                handler.clearObjects();
                if(scoreKeep%1050==0){
                    spawnBoss1(false);
                }
            }

            if(hud.getLevel()==5){
                wallBounceEnemy(2);
                trackingEnemy(1);
            }

            if(hud.getLevel()==6){
                handler.clearObjects();
                if(scoreKeep%1050==0){
                    spawnBoss1(false);
                    spawnBoss1(true);
                    trackingEnemy(1);
                }
            }

            if(hud.getLevel()==7){
                trackingEnemy(3);
                healthPod(3);
            }
            //procedulely generated levels
            if(hud.getLevel()>7 && scoreKeep%1000==0){
                handler.clearObjects();
                if(scoreKeep%1050==0){
                    if(r.nextInt(100)<5){
                        specialPod(1);
                    }
                    if(hud.getLevel()%5==0){
                        healthPod(1);
                    }
                    if(hud.getLevel()%10==0){
                        spawnBoss1(false);
                        if(scoreKeep>10000 && r.nextInt(10)>3){
                            spawnBoss1(true);
                        }
                        trackingEnemy(r.nextInt(2)+1);
                        disruptEnemy(r.nextInt((int)hud.getLevel()));
                    }else{
                        wallBounceEnemy(r.nextInt((int)hud.getLevel())+1);
                        if(r.nextInt(10)>3){
                            disruptEnemy(r.nextInt((int)hud.getLevel()));
                        }
                        if(r.nextInt(10)>5){
                            fastEnemy(r.nextInt((int)hud.getLevel()));
                        }
                        if(r.nextInt(10)>7){
                            trackingEnemy(r.nextInt((int)hud.getLevel()));
                        }
                    }
                }
            }
        }
    }

    public void spawnBoss1(boolean left){
        handler.addObject(new BossEnemy((float)(610),(float)(-100),ID.Boss, handler, left)); 
    }

    public void wallBounceEnemy(int x){
        for(int i=0;i<x;i++){
            handler.addObject(new WallBouncingEnemy((float)r.nextInt((int)(Game.WIDTH-50)),(float)r.nextInt((int)(Game.HEIGHT-50)),ID.Enemy, handler));
        }
    }

    public void disruptEnemy(int x){
        for(int i=0;i<x;i++){
            handler.addObject(new DisruptEnemy((float)r.nextInt((int)(Game.WIDTH-50)),(float)r.nextInt((int)(Game.HEIGHT-50)),ID.DisruptEnemy, handler));
        }
    }

    public void fastEnemy(int x){
        for(int i=0;i<x;i++){
            handler.addObject(new FastEnemy((float)r.nextInt((int)(Game.WIDTH-50)),(float)r.nextInt((int)(Game.HEIGHT-50)),ID.Enemy, handler));
        }
    }

    public void healthPod(int x){
        for(int i=0;i<x;i++){
            handler.addObject(new HealthPod((float)r.nextInt((int)(Game.WIDTH-150)),(float)r.nextInt((int)(Game.HEIGHT-150)),ID.HealthPod, handler));
        }
    }

    public void specialPod(int x){
        for(int i=0;i<x;i++){
            handler.addObject(new SpecialPod((float)r.nextInt((int)(Game.WIDTH-150)),(float)r.nextInt((int)(Game.HEIGHT-150)),ID.SpecialPod, handler));
        }
    }

    public void trackingEnemy(int x){
        for(int i=0;i<x;i++){
            handler.addObject(new TrackingEnemy((float)r.nextInt((int)(Game.WIDTH-150)),(float)r.nextInt((int)(Game.HEIGHT-150)),ID.TrackingEnemy, handler));
        }
    }

    public void popUpEnemy(int x){
        for(int i=0;i<x;i++){
            handler.addObject(new popUpEnemy((float)r.nextInt((int)(Game.WIDTH-50)),(float)r.nextInt((int)(Game.HEIGHT-50)),ID.Enemy, handler));
        }
    }
}
