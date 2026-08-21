# Example records

Test records for [schema.json](../schema.json). They are fixtures for the
repository checks, not guidance. [taxonomy.md](../taxonomy.md) defines the
classifications and [INTEGRATION.md](../INTEGRATION.md) covers implementation.

`tools/check_standard.py` reads every `.json` file here. A file whose name
begins with `valid-` must validate against the schema. A file whose name
begins with `invalid-` must fail. Checking both directions matters: a change
that quietly widened the schema would still let the valid records pass, and
only the invalid ones would catch it.

| File | What it covers |
| --- | --- |
| `valid-no-ai.json` | The minimum record. Both required fields, no descriptors. |
| `valid-assistive-ai.json` | Assistive AI carries no descriptors. |
| `valid-generative-ai-no-descriptors.json` | Descriptors are optional on Generative AI. |
| `valid-generative-ai-with-descriptors.json` | Two descriptors on a Generative AI record. |
| `invalid-classification-outside-enum.json` | A classification value HPF does not define. |
| `invalid-missing-taxonomy-version.json` | The version field is required, so a classification alone is not a record. |
| `invalid-descriptors-on-assistive.json` | Descriptors apply only to Generative AI. |
| `invalid-descriptor-outside-enum.json` | A descriptor value the schema does not list. |
| `invalid-empty-descriptors.json` | An empty array. Omit the field instead. |
| `invalid-taxonomy-version-format.json` | The version field takes `MAJOR.MINOR` only. |

The last one records a real limitation rather than a mistake. The schema
cannot express which revision of 0.9 a declaration used, because every
revision of the consultation draft is taxonomy version 0.9. That is an open
question for the consultation, not something to work around by loosening the
pattern.

## Adding a record

Name it for the case it covers, prefixed `valid-` or `invalid-`, and add a row
to the table above. Run `python3 tools/check_standard.py` before committing.

There is no record here for a production with no declaration, because there is
no such record. Where no HPF declaration exists, omit the record entirely. An
absent record and No AI Used are different states.
