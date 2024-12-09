import javax.swing.JFrame;  //подключаем контейнер JFrame библиотеки Swing

public class Main_class {   //создание окна 
	public static void main(String[] args) {   //метода класса Main
		JFrame obj = new JFrame();    //создание обЪекта JFrame(пустое окно)
		Gameplay game = new Gameplay();       //создаем объект класса Gameplay
		obj.setBounds(10,10,700,600);   //задает размеры окна
		obj.setTitle("BRICK BREAKER");    //определение названия окна
		obj.setResizable(false);      //определяем, что размеры окна нельзя менять
		obj.setVisible(true);          //сделать окно видимым
		obj.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);     //определение действия при завершении программы
		obj.add(game);                                //добавлние геймплея
	}
}
