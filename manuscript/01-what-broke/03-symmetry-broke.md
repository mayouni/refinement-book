# §1.3 The symmetry broke

That last sentence is the entire problem this book exists to address.

For most of the history of computing, knowing whether a change was correct was bounded by the speed at which a human could write it. A human wrote a few lines, tested them, looked at the surrounding code, asked a colleague, ran the suite of regression tests, and over the course of an hour or a day developed a quiet conviction that the change was sound. The development cycle was paced by the writer's pace. The reviewer was usually the writer.

That symmetry broke somewhere around the middle of the 2020s. Not all at once, not for every team, but irreversibly. By the time the directive arrived on Amina's desk, the writers were no longer all human. The writers were agents — fast, careful, capable, increasingly uncomplaining. The reviewers were still human, but the volume of work passing through them had multiplied by an order of magnitude, then by another order of magnitude, and showed no sign of slowing.

> **The text diff.** The unit of change that won the previous decade. It was built for a world where one human read what another human had written. It does not survive at agent throughput.

The bottleneck moved. It moved from the writing of code to the review of code, and then to the broader question of which changes were worth landing at all. The old assumption that the writer and reviewer were the same person ceased to hold. The old artefact that mediated their work — the text diff, the line-by-line patch — ceased to scale.

What the discipline this book describes proposes is a different artefact, a different review surface, a different way of asking the question "is this change correct?" — and a different way of answering it.

It is not, in the end, a complicated idea. Programmers in regulated industries had been carrying parts of it for decades. Auditors had been demanding parts of it for longer. The technology arrived to compose those parts into something workable in the same season the bottleneck made the composition necessary.

Sonibank Niger did not invent any of these parts. The bank inherited some of them from the regulatory framework imposed by BCEAO and the Organization for the Harmonization of Business Law in Africa. Others it borrowed from older traditions of careful change management in mature engineering organizations. A few it had to design itself, working with a small team of programmers and a single methodologist over the course of a year and a half.

The result was not a product. The result was a way of working that, viewed in retrospect, had a name. The name is the title of this book.
