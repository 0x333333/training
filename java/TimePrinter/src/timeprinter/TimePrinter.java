package timeprinter;

import java.util.Date;

/**
 *
 * @author zhipeng
 */
public class TimePrinter extends Thread {

    private int pauseTime;
    private String n;

    TimePrinter(int pauseTime, String n) {
        this.pauseTime = pauseTime;
        this.n = n;
    }

    public void run() {
        while (true) {
            try {
                System.out.println(n + ":" + new Date(System.currentTimeMillis()));
                Thread.sleep(pauseTime);
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }

    public static void main(String[] args) {
        TimePrinter tp1 = new TimePrinter(1000, "TimePrinter 1");
        tp1.start();
        TimePrinter tp2 = new TimePrinter(3000, "TimePrinter 2");
        tp2.start();
    }

}
