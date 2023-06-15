#include "lists.h"

/**
 * print_dlistint - print all the elements of a
 * dlistint_t list
 *
 * @h: head of the list
 * return: the number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	int arry;

	arry = 0;

	if (i == NULL)
		return (arry);

	while (i->prev != NULL)
		i = i->prev;

	while (i != NULL)
	{
		printf("%d\n", i->n);
		arry++;
		i = i->next;
	}

	return (arry);
}

