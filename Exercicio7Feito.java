/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package exercicio7feito;


import java.util.Random;

public class Exercicio7Feito {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
            // --- Passo 1: Definir o tamanho e criar as matrizes ---

        final int NUMERO_DE_LINHAS = 6;
        final int NUMERO_DE_COLUNAS = 4;

        int[][] matrizOriginal = new int[NUMERO_DE_LINHAS][NUMERO_DE_COLUNAS];

        // Criamos um objeto 'Random' que será nossa fábrica de números aleatórios // <<< MUDANÇA
        Random random = new Random();
        
        // A linha abaixo não é mais necessária se vamos preencher automaticamente.
        // Scanner scanner = new Scanner(System.in);

        System.out.println("--- Preenchendo a Matriz 6x4 com números aleatórios ---"); // <<< MUDANÇA

        for (int i = 0; i < NUMERO_DE_LINHAS; i++) { // Loop para as linhas
            for (int j = 0; j < NUMERO_DE_COLUNAS; j++) { // Loop para as colunas
                // A parte de pedir para o usuário foi substituída pela linha abaixo:
                // System.out.print("Digite o valor para a Linha " + (i + 1) + ", Coluna " + (j + 1) + ": ");
                // matrizOriginal[i][j] = scanner.nextInt();
                
                // random.nextInt(100) gera um número de 0 a 99.
                // Somamos 1 para que os números sejam de 1 a 100.
                matrizOriginal[i][j] = random.nextInt(100) + 1; // <<< MUDANÇA
            }
        }

        // --- Passo 2: Calcular a matriz resultante ---
        // (O restante do código continua exatamente igual)

        int[][] matrizResultante = new int[NUMERO_DE_LINHAS][NUMERO_DE_COLUNAS];

        for (int i = 0; i < NUMERO_DE_LINHAS; i++) {
            for (int j = 0; j < NUMERO_DE_COLUNAS; j++) {
                matrizResultante[i][j] = matrizOriginal[i][j];
            }
        }
        
        for (int i = 0; i < NUMERO_DE_LINHAS; i++) {
            int maiorElementoDaLinha = matrizResultante[i][0];
            for (int j = 1; j < NUMERO_DE_COLUNAS; j++) {
                if (matrizResultante[i][j] > maiorElementoDaLinha) {
                    maiorElementoDaLinha = matrizResultante[i][j];
                }
            }

            for (int j = 0; j < NUMERO_DE_COLUNAS; j++) {
                matrizResultante[i][j] = matrizResultante[i][j] * maiorElementoDaLinha;
            }
        }

        // --- Passo 3: Mostrar as matrizes ---
        
        System.out.println("\n=============================================");
        System.out.println("--- Matriz Original (Gerada aleatoriamente) ---");
        for (int i = 0; i < NUMERO_DE_LINHAS; i++) {
            for (int j = 0; j < NUMERO_DE_COLUNAS; j++) {
                System.out.print(matrizOriginal[i][j] + "\t");
            }
            System.out.println();
        }

        System.out.println("\n--- Matriz Resultante (Após os cálculos) ---");
        for (int i = 0; i < NUMERO_DE_LINHAS; i++) {
            for (int j = 0; j < NUMERO_DE_COLUNAS; j++) {
                System.out.print(matrizResultante[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println("=============================================");


        
    }
    
}
