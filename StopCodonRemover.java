package com.company;

import java.util.Scanner;

public class StopCodonRemover {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String userSequence;
        System.out.println("Please enter nucleotide sequence: ");
        userSequence = input.nextLine();
        System.out.println("Your nucleotide sequence without stop codons is: " +
                stopToNoStop(userSequence));

    }

    public static String stopToNoStop (String userSequence){
        String thymine [] = {"TAG", "TAA", "TGA", " "};
        String any [] = {"---", ""};
        userSequence = userSequence.replace(thymine[0], any[0]);
        userSequence = userSequence.replace(thymine[1], any[0]);
        userSequence = userSequence.replace(thymine[2], any[0]);
        userSequence = userSequence.replace(thymine[3], any[1]);
        return userSequence;
    }
}
