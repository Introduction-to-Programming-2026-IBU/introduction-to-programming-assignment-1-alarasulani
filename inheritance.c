#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Each person has two parents and two alleles
#define GENERATIONS 3
#define INDENT_LENGTH 4

typedef struct person
{
    struct person *parents[2]; // NULL if no parents
    char alleles[2];           // 'A', 'B', or 'O'
} person;

// Function prototypes
person *create_family(int generations);
void free_family(person *p);
void print_family(person *p, int generation);
void print_codes(void);
char random_allele(void);

int main(void)
{
    srand(time(0));

    person *p = create_family(GENERATIONS);
    print_family(p, 0);
    free_family(p);

    return 0;
}

person *create_family(int generations)
{
    // TODO: allocate memory for a new person
    person *p = malloc(sizeof(person));

    if (p == NULL)
    {
        return NULL;
    }

    if (generations > 1)
    {
        person *parent0 = create_family(generations - 1);
        person *parent1 = create_family(generations - 1);

        p->parents[0] = parent0;
        p->parents[1] = parent1;

        // TODO: randomly inherit one allele from each parent
        p->alleles[0] = p->parents[0]->alleles[rand() % 2];
        p->alleles[1] = p->parents[1]->alleles[rand() % 2];
    }
    else
    {
        // oldest generation — no parents, random alleles
        p->parents[0] = NULL;
        p->parents[1] = NULL;
        p->alleles[0] = random_allele();
        p->alleles[1] = random_allele();
    }

    return p;
}

void free_family(person *p)
{
    // base case — if p is NULL, return
    if (p == NULL)
    {
        return;
    }

    free_family(p->parents[0]);
    free_family(p->parents[1]);

    free(p);
}

// Print each family member and their blood type
void print_family(person *p, int generation)
{
    if (p == NULL)
    {
        return;
    }

    // Print parents before child
    print_family(p->parents[0], generation + 1);
    print_family(p->parents[1], generation + 1);

    // Indent based on generation
    for (int i = 0; i < generation * INDENT_LENGTH; i++)
    {
        printf(" ");
    }

    // Print the generation label and blood type
    if (generation == 0)
    {
        printf("Child (Generation %i): blood type %c%c\n", generation, p->alleles[0],
               p->alleles[1]);
    }
    else if (generation == 1)
    {
        printf("Parent (Generation %i): blood type %c%c\n", generation, p->alleles[0],
               p->alleles[1]);
    }
    else
    {
        printf("Grandparent (Generation %i): blood type %c%c\n", generation, p->alleles[0],
               p->alleles[1]);
    }
}

// Randomly choose an allele: 'A', 'B', or 'O'
char random_allele(void)
{
    int r = rand() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}
