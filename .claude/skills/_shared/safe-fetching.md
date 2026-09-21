# Safe fetching

Shared by every research skill in this repository and by the worker briefs they hand out.

## Why this exists

On 2026-09-21 a name-collision check told a worker to "fetch `<name>.com` and see what is
hosted there". The worker ran `curl` against a string of parked and unknown domains, one of
them served a page the owner's antivirus quarantined, and the saved copy had to be removed
by hand. Nothing in the research needed the page's content. The question was only whether
the domain was taken.

Parked domains, domain-sale landers and abandoned sites are where drive-by scripts and
malicious redirects live. A research worker gains nothing from their content and puts the
owner's machine at risk by downloading it.

## The rule

Do not fetch a host you cannot name the publisher of. This covers `curl`, `wget`,
WebFetch, a browser tool, and any script that downloads a URL (including
`_shared/jev/sources.py`).

- **Whether a domain is taken is a DNS question.** Answer it with `dig +short <domain>` (or
  `host`), and report "A record present" or "no A record". Never open the site to see what
  is there, and never save its response to disk.
- **Fetch only hosts whose publisher is known and accountable**, for example:
  GitHub (including `raw.githubusercontent.com` and the `gh` CLI), package registries and
  their indexes (Homebrew `formulae.brew.sh`, npm, PyPI, crates.io), app stores, the
  official documentation or site of a vendor or project already identified by name, source
  hosts of major projects (`chromium.googlesource.com`, WebKit, Mozilla), Wikipedia,
  established media, and the large forums (Hacker News, Reddit, Stack Overflow).
- **A host that only surfaced in search results stays unopened.** Report what the search
  snippet shows, give the URL, mark the finding `確度: 中` or `低`, and write `未取得` so the
  caller knows nobody read the page. The caller decides whether it is worth opening by hand.
- **Guessed URLs are unknown hosts.** Constructing `<candidate-name>.com`, `.app`, `.io`
  and the like and requesting it is exactly the failure above, whatever the TLD.
- **Pipe, do not save.** When a known host is fetched from the shell, pipe the response to
  the filter that reads it (`curl -s … | grep …`) or write it under the session scratchpad.
  Do not leave downloaded pages in `/tmp`.
- When unsure whether a host counts as known, treat it as unknown. A finding marked `未取得`
  costs the research little. A quarantined download costs the owner's trust in the tooling.

## For the caller

- Put this rule into every worker prompt that may touch the network: the briefs under
  `references/agents/` carry a one-line version that points here, and an ad-hoc prompt
  needs the same line.
- Before running `sources.py`, drop the URLs on hosts this rule would not fetch. They are
  the `未取得` findings and stay unconfirmed.
- Never write a task in the form "fetch X and see what is there" for a host nobody has
  identified. Ask instead for the DNS answer or for what search results say.
