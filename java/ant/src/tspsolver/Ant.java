package tspsolver;
import java.util.Random;

public class Ant {
    
	public int[]tour;
	public double tourlength;
    int citys;
	int[] unvisitedcity;  // 1: unvisted, 0: visited
    
    public void SelectCity(int citycount, int index){
        citys = citycount;
        unvisitedcity = new int[citycount];
        tour = new int[citycount+1];
        tourlength = 0;
        for(int i = 0; i < citycount; i++){
            tour[i] = -1;
            unvisitedcity[i] = 1;
        }
        unvisitedcity[index] = 0;
        tour[0] = index;
    }
    
    public void SelectNextCity(int index, double[][]tao, double[][]distance){
        double []p;
        p = new double[citys];
        double alpha=1.0;
        double beta=1.0;
        double sum=0;
        int currentcity=tour[index-1];

        for(int i = 0; i < citys; i++){
            if(unvisitedcity[i]==1)
                sum += (Math.pow(tao[currentcity][i], alpha) *
                        Math.pow(1.0/distance[currentcity][i], beta));
        }

        for(int i = 0; i < citys; i++){
            if(unvisitedcity[i]==0)
                p[i]=0.0;
            else{
                p[i]=(Math.pow(tao[currentcity][i], alpha)*
                      Math.pow(1.0/distance[currentcity][i], beta))/sum;
            }
        }
        
        long r1 = System.currentTimeMillis();
        Random rnd=new Random(r1);
        double selectp=rnd.nextDouble();
        
        double sumselect=0;
        int selectcity=-1;
        for(int i = 0; i < citys; i++){
            sumselect += p[i];
            if(sumselect >= selectp){
                selectcity = i;
                break;
            }
        }
        
        if (selectcity==-1) {
            System.out.println(selectcity+"");
            return;
        }
        
        tour[index]=selectcity;
        unvisitedcity[selectcity]=0;
    }
    
    public void CalTourLength(double [][]distance){
        tourlength=0;
        tour[citys] = tour[0];
        for(int i = 0; i < citys; i++){
            tourlength += distance[tour[i]][tour[i+1]];
        }    
    }
}
