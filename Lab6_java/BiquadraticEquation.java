import java.util.ArrayList;
import java.util.List;

class BiquadraticEquation {
    private final double a;
    private final double b;
    private final double c;

    public BiquadraticEquation(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public List<Double> getRoots() {
        List<Double> roots = new ArrayList<>();
        double D = b * b - 4 * a * c;

        if (D > 0) {
            double sqD = Math.sqrt(D);
            double y1 = (-b + sqD) / (2.0 * a);
            double y2 = (-b - sqD) / (2.0 * a);
            if (y1 >= 0) {
                roots.add(Math.sqrt(y1));
                roots.add(-Math.sqrt(y1));
            }
            if (y2 >= 0) {
                roots.add(Math.sqrt(y2));
                roots.add(-Math.sqrt(y2));
            }
        } else if (D == 0) {
            double y = -b / (2.0 * a);
            if (y >= 0) {
                roots.add(Math.sqrt(y));
                roots.add(-Math.sqrt(y));
            }
        }else if (D < 0) {
            return roots;
        }
        
        return roots;
     }
}