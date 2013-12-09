package tspsolver;
import java.io.*;

public class ACO {
	
    Ant []ants;
    int antcount;        // Nombre de fourmis
    int citycount;       // Nombre de villes
    double [][]distance; // Tableau de distance parmi les villes
    double [][]tao;      // Tableau de phéromone
    double []besttour;   // Meilleur solution
    double bestlength;   // Meilleur distance 

    /**
     *@param filename donnée de villes
     *@throws si le fichier n'existe pas
    */
    public void init(String filename) throws FileNotFoundException, IOException{
    	// Sauvégarder les données de position pour chaque ville
        double[] x;
        double[] y;
        
        String strbuff;
        BufferedReader tspdata = new BufferedReader(new InputStreamReader(new FileInputStream(filename)));
        strbuff = tspdata.readLine();
        
        citycount = Integer.valueOf(strbuff);
        antcount = citycount;
        ants = new Ant[antcount];
        distance = new double[citycount][citycount];
        x = new double[citycount];
        y = new double[citycount];
        
        for (int citys = 0; citys < citycount; citys++) {
            strbuff = tspdata.readLine();
            String[] strcol = strbuff.split(" ");
            x[citys] = Double.valueOf(strcol[1]);
            y[citys] = Double.valueOf(strcol[2]);
        }
        
        // Calculer les distances
        for (int city1 = 0; city1 < citycount - 1; city1++) {
            distance[city1][city1] = 0;
            for (int city2 = city1 + 1; city2 < citycount; city2++) {
                distance[city1][city2] = (Math.sqrt((x[city1] - x[city2]) * (x[city1] - x[city2])
                        + (y[city1] - y[city2]) * (y[city1] - y[city2])));
                distance[city2][city1] = distance[city1][city2];
            }
        }
        distance[citycount - 1][citycount - 1] = 0;
        
        // Initialiser la tableau de phéromone
        tao = new double[citycount][citycount];
        for(int i = 0; i < citycount; i++)
        {
            for(int j = 0; j < citycount; j++){
                tao[i][j] = 0.1;
            }
        }
        
        bestlength = Double.MAX_VALUE;
        besttour = new double[citycount+1];
        
        // Placer une fourmi sur chaque ville
        for(int i=0;i<antcount;i++){
            ants[i]=new Ant();
            ants[i].SelectCity(citycount, i);
        }
    }

    public void run(int maxruntimes){
        for(int runtimes = 0; runtimes < maxruntimes; runtimes++){
            for(int i = 0; i < antcount; i++){
                for(int j = 1; j < citycount; j++){
                    ants[i].SelectNextCity(j, tao, distance);
                }
                // Calculer la distance pour chaque fourmi
                ants[i].CalTourLength(distance);
                if(ants[i].tourlength<bestlength){
                    // Sauvégarder la meilleur solution 
                    bestlength=ants[i].tourlength;
//                    System.out.println(runtimes+": "+bestlength);
                    for(int j = 0; j < citycount+1; j++)
                        besttour[j] = ants[i].tour[j];
                }
            }

            UpdateTao();
            
            for(int i=0;i<antcount;i++){
                ants[i].SelectCity(citycount, i);
            }
        }
    }
    
    /**
     * Mettre à jour la tableau de phéromone
     */
    private void UpdateTao(){
        double C = 0.7;   // La coefficient d'évaporation C
        double Q = 1.0;   // La constante Q

        for(int i = 0; i < citycount; i++)
            for(int j = 0; j < citycount; j++)
                tao[i][j]=tao[i][j]*(1-C);
        
        for(int i = 0; i < antcount; i++){
            for(int j=0;j<citycount;j++){
                tao[ants[i].tour[j]][ants[i].tour[j+1]] += Q/ants[i].tourlength;
            }
        }
    }
    
    /**
     * Aficher la résultat
     */
    public void ReportResult(){
        System.out.println("La meilleur solution est: " + bestlength);
    }
}
