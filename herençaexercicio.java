/*
    Crie uma classe com os seguintes atributos de um analista de sistemas: 
    - Nome, 
    - ano de nascimento, 
    - salário base, 
    - se tem mestrado, 
    - meses de experiência.

    Crie uma classe com os seguintes atributos de um programador:
    - Tem graduação, 
    - salário base, 
    - se tem certificação Java, 
    - nome, 
    - sexo, 
    - ano de nascimento.

    Tanto os programadores quantos os analistas de sistemas são tipos de 
    funcionário.

    Aplique o conceito de encapsulamento e de herança.

    Na classe do método main, instancie um objeto do tipo programador e 
    chame o método que exibe todas as informações cadastrais. 
    
    Cada classe possui um método chamado “exibe()” que dá um "System.out.println"
    nos campos da classe; apenas as classes filhas podem executar o método 
    “exibe()” da classe mãe.

 */
package exercicioheranca1;

public class Principal {

    public static void main(String[] args) {
        //instancia um programador com dados de exemplo
        Programador prog = new Programador(
        "Henrique santos",  //nome
         1999,              //ano de nascimento
         5500.75,           //salario base
         true,              //tem graduação
         true,              //tem certificado
        "masculino"         // sexo
      );   
        //chama o metedo que exibe todas as informaçoes (mae + filho)
        prog.exibe();
    }
        
}
   // classe mãe (funcionario)
    class Funcionario{
        //encapsulamento: atributo privados
        private String nome;
        private int anoNascimento;
        private double salarioBase;
        
        // contrutor
        public Funcionario(String nome, int anoNascimento, double salarioBase){
            this.nome = nome;
            this.anoNascimento = anoNascimento;
            this.salarioBase= salarioBase;
        }
        //getters e setters(permitem acesso controlado aos atributos)
        public String getnome() { return nome;}
        public void setNome(String nome){this.nome = nome;}
        
        public int getAnoNascimento(){return anoNascimento; }
        public void setAnoNascimento(int anoNascimento){this.anoNascimento = anoNascimento;}
        
        public double getSalarioBase(){return salarioBase;}
        public void setSalarioBase(double salarioBase) { this.salarioBase=salarioBase;}
        
        //metodo que exibe classe mãe protegido para que apenas subclasses e clases do mesmo pacote
        //possam executalo diretamente. ele imprime os campos da mãe   
        protected void exibe(){
            System.out.println("== Dados do Funcinario (filho)==" );
            System.out.println("Nome: " + nome);
            System.out.println("Ano de nascimento: " + anoNascimento);
            System.out.println("Salario base: " + salarioBase);  
        }
        //Classe analista que herda de funcionario
        class Analista extends Funcionario {
            private boolean temMestrado;
            private int mesesExperiencia;
            
            public Analista(String nome, int anoNascimento, double salarioBase, 
                    boolean temMestrado, int mesesExperiencia) {
                super(nome, anoNascimento, salarioBase);
                this.temMestrado = temMestrado;
                this.mesesExperiencia = mesesExperiencia;
            }
            public boolean isTemMestrado(){ return temMestrado;}
            public void setTemMestrado(boolean temMestrado){this.temMestrado= temMestrado;}
            
            public int getMesesExperiencia(){return mesesExperiencia;}
            public void setMesesExperiencia(int mesesExperiencia){this.mesesExperiencia=mesesExperiencia;}
            
            //Método exibe da filha: público — chama o exibe() da mãe (protected) e depois mostra os campos da filha
            @Override
            public void exibe(){
                super.exibe();//so classes filhas conseguem chamar este metodo da mae
                System.out.println("Tem mestrado" + (temMestrado ? "sim" : "nao"));
                System.out.println("meses de experiencia: " + mesesExperiencia);
            }
       }
    }
    class Programador extends Funcionario {
        private boolean temGraduacao;
        private boolean temCertificacaoJava;
        private String sexo;
        
        public Programador(String nome, int anoNascimento, double salarioBase,
                boolean temGraduacao, boolean temCertificacaoJava, String sexo){
            super(nome, anoNascimento, salarioBase);
            this.temGraduacao = temGraduacao;
            this.temCertificacaoJava = temCertificacaoJava;
            this.sexo = sexo;
        }
        public boolean isTemgraduacao(){ return temGraduacao;}
        public void setTemGraduacao(boolean temGraduacao){this.temGraduacao = temGraduacao;}
        
        public boolean isTemCertificacaoJava() {return temCertificacaoJava;}
        public void setTemCertificacaoJava(boolean temCertificacaoJava) { this.temCertificacaoJava = temCertificacaoJava;}
        
        public String getSexo(){ return sexo;}
        public void  setSexo(String sexo){ this.sexo = sexo;}
        
         // Exibe: chama super.exibe() (que imprime os campos da mãe) e depois os campos do programador
         @Override
         public void exibe(){
            super.exibe();
            System.out.println("Dados do Programador (Filha)");
            System.out.println("Tem graduacao: " + (temCertificacaoJava ? "sim" : "nao"));
            System.out.println("Tem certificacao java: " + (temCertificacaoJava? "sim" : "nao"));
            System.out.println("Sexo" + sexo);
         }
    }
    


