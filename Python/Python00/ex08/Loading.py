def ft_tqdm(lst: range) -> None:
    """
    Takes the elements iterates through the list of elements.
    Yields the element, so it can be used. TQDM is only to print status
    """
    nbElem = len(lst)
    for i, elem in enumerate(lst, 1):
        progressPercent = float(i / nbElem)
        sizebar = 150
        bar = ("=" * int(progressPercent * sizebar) + ">"
               + " " * int((1 - progressPercent) * sizebar))
        print(f"{int(progressPercent * 100)}%|{bar}| {i}/{nbElem}\r",
              end='', flush=True)
        yield elem
