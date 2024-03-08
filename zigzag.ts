const text = ` This guide is intended to aid advanced Go users in better understanding their application costs by providing insights into the Go garbage collector. It also provides guidance on how Go users may use these insights to improve their applications' resource utilization. It does not assume any knowledge of garbage collection, but does assume familiarity with the Go programming language.
The Go language takes responsibility for arranging the storage of Go values; in most cases, a Go developer need not care about where these values are stored, or why, if at all. In practice, however, these values often need to be stored in computer physical memory and physical memory is a finite resource. Because it is finite, memory must be managed carefully and recycled in order to avoid running out of it while executing a Go program. It's the job of a Go implementation to allocate and recycle memory as needed.
Another term for automatically recycling memory is garbage collection. At a high level, a garbage collector (or GC, for short) is a system that recycles memory on behalf of the application by identifying which parts of memory are no longer needed. The Go standard toolchain provides a runtime library that ships with every application, and this runtime library includes a garbage collector.
Note that the existence of a garbage collector as described by this guide is not guaranteed by the Go specification, only that the underlying storage for Go values is managed by the language itself. This omission is intentional and enables the use of radically different memory management techniques.
Therefore, this guide is about a specific implementation of the Go programming language and may not apply to other implementations. Specifically, this following guide applies to the standard toolchain (the gc Go compiler and tools). Gccgo and Gollvm both use a very similar GC implementation so many of the same concepts apply, but details may vary.
Furthermore, this is a living document and will change over time to best reflect the latest release of Go. This document currently describes the garbage collector as of Go 1.19.`

// Output book as a website
const WRAP = 80;

let wrapCount = 0;
const wrappedText = text.split(' ').reduce((acc: string, word: string) => {
    wrapCount += word.length;
    if (wrapCount >= WRAP) {
        wrapCount = wrapCount % WRAP;
        return acc + '\n' + word + ' ';
    }
    return acc + word + ' ';
}, "");

wrappedText.split('\n').forEach((line: string, i: number) => {
    if (i % 2 === 0) {
        line = line.endsWith('.') ? line + '\n' : line;
        console.log('--> ' + line);
        return;
    }

    line = line.split(' ').map((word: string) => {
        word = word.replace(/[^a-zA-Z., ]/g, '');
        if (word.endsWith('.')) {
            return '.' + word.slice(0, -1);
        } else if (word.endsWith(',')) {
            return ', ' + word.slice(0, -1);
        }
        return word;

    }).reverse().join(' ').trim();

    console.log(line + ' <--');
});
