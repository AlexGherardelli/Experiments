/****************************************************************************
 * dictionary.c
 *
 * Computer Science 50
 * Problem Set 5
 *
 * Implements a dictionary's functionality.
 ***************************************************************************/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#include "dictionary.h"

#define HASHTABLE_SIZE 65536

// Declare hashtable
node* hashtable[HASHTABLE_SIZE];

int dict_size = 0;
char words[LENGTH + 1];

/*
* Hashing function provided on Reddit: 
* https://www.reddit.com/r/cs50/comments/1x6vc8/pset6_trie_vs_hashtable/
*/
int hash(const char* needs_hashing)
{
    unsigned int hash = 0;
    for (int i = 0, n = strlen(needs_hashing); i < n; i++)
        hash = (hash << 2) ^ needs_hashing[i];
    return hash % HASHTABLE_SIZE;
}




/**
 * Loads dictionary into memory.  Returns true if successful else false.
 */
bool load(const char* dictionary)
{
    // Array of chars
    char words_array[LENGTH + 1];
    
    // Open file
    FILE* dict = fopen(dictionary, "r");
    
    // Check if dict is NULL
    if (dict == NULL)
    {
        printf("Couldn't open the dictionary file\n");
        return false;
    }
    while(fscanf(dict, "%s", words_array) != EOF)
    {
        // allocate space for new_node
        node* new_word = malloc(sizeof(node));
        
        // Copy new word in array
        strcpy(new_word -> word, words_array);

        
        int index = hash(words_array);

        dict_size++;
        
       // if hashtable is empty
       if (hashtable[index] == NULL)
       {
           //DO something
           hashtable[index] = new_word;
           new_word -> next = NULL;
           
       }
       else
       {
           // Append to linked list
           new_word -> next = hashtable[index];
           hashtable[index] = new_word;
           
       }
       
    
    }
    //printf( "Total word count = %i\n", dict_size);

    
    // close file
    fclose(dict);

    return true;
}

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char* word)
{
    // Lower all letters for word
    char unchecked[LENGTH + 1];
    int len = strlen(word);

    for (int i = 0; i < len; i++)
    {
        unchecked[i] = tolower(word[i]);
    }
    unchecked[len] = '\0';
    

    // Set a crawler to point for hashtable[index]
    int index = hash(unchecked);
    node* crawler = hashtable[index];
    
    // Return false if hashtable is empty
    if (crawler == NULL)
    {
        return false;
    }
    
    // Check for words until the end of the linked list
    while (crawler != NULL)
    {
        if(strcmp(crawler -> word, unchecked) == 0)
        {
            return true;
        }
        crawler = crawler -> next;
    }
   
    return false;
}


/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    // Returns dict size
    return dict_size;
}

/**
 * Unloads dictionary from memory.  Returns true if successful else false.
 */
bool unload(void)
{
    // loop until the end of hashtable
    for (int i = 0; i < HASHTABLE_SIZE; i++)
    {
        // check if hashtable is empty
        if(hashtable[i] == NULL)
        {
            i++;
        }
        else
        {
            // loop until the end of linked list
            while(hashtable[i] != NULL)
            {
                // set a cursor to point at the node
                node* cursor = hashtable[i];
                // set hastable to be equal to next cursor node
                hashtable[i] = cursor -> next;
                // free!
                free(cursor);
                
            }
            
            i++;
        }

    }
    // that's all folks!
    return true;
    
    /*
        // prompt user for number
    printf("Number to search for: ");
    int n = GetInt();

    // get list's first node
    node* ptr = first;

    // search for number
    while (ptr != NULL)
    {
        if (ptr->n == n)
        {
            printf("\nFound %i!\n", n);
            sleep(1);
            break;
        }
        ptr = ptr->next;
    }*/

}
