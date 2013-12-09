package tspsolver;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {
    public static void main(String[] args) {
        ACO aco = new ACO();
        try {
        	// Lancer la systhème par lissant les données de villes
            aco.init("test.tsp");
            // Configurer la nombre de boucle
            aco.run(100);
            // Aficher la résultat
            aco.ReportResult();
        } catch (FileNotFoundException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
