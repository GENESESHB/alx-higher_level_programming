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

	if (h == NULL)
		return (arry);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		arry++;
		h = h->next;
	}

	return (arry);
}

