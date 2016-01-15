/**
 * recover.c
 *
 * Computer Science 50
 * Problem Set 4
 *
 * Recovers JPEGs from a forensic image.
 */
 
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
 
#define BLOCK 512

int main(void)
{
    // initialize buffer of size 512
    uint8_t buffer[BLOCK];
    
    // open card file
    FILE* card = fopen("card.raw", "r");
    
    // initialize string for title
    char title[8];
    
    // initialize counter
    int count = 0;
    
    // initialize pointer for recovered files
    FILE* recovered;
    
    if (card == NULL)
    {
      printf("Could not open the %s file\n", "card.raw");
      return 1;
    }
    
    
    while (fread(buffer, BLOCK, 1, card) != 0)
    {

      if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] == 0xe0 || buffer[3] == 0xe1))
      {
        if(count == 0)
        {
          sprintf(title, "%03d.jpg", count);
          recovered = fopen(title, "a");
          fwrite(&buffer, BLOCK, 1, recovered);
          count++;
        }
        else
        {
          fclose(recovered);
          sprintf(title, "%03d.jpg", count);
          recovered = fopen(title, "a");
          fwrite(&buffer, BLOCK, 1, recovered);
          count++;
          
        }
      }
      else
      {
        if (count > 0)
        {
          fwrite(&buffer, BLOCK, 1, recovered);
        }
      }

        
    }


    fclose(card);
    return 0;
    
}
