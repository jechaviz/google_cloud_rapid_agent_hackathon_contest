# Rules checklist

Verificado el 2026-05-29 contra Devpost rules y overview.

## Fechas

- [ ] Contest period: 2026-05-05 a 2026-06-11.
- [ ] Deadline final: 2026-06-11 14:00 PDT / 15:00 America/Mexico_City.
- [ ] Solicitud de creditos Google Cloud, si aplica: antes de 2026-06-04.
- [ ] Freeze interno: 2026-06-10 20:00 America/Mexico_City.

## Elegibilidad y equipo

- [ ] Confirmar edad legal de mayoria y jurisdiccion elegible.
- [ ] Si es equipo, maximo 4 personas y todos agregados al proyecto Devpost.
- [ ] Representante autorizado definido si se sube como equipo/organizacion.
- [ ] No incluir datos personales sensibles en repo, video o screenshots.

## Build requirements

- [x] Proyecto nuevo para el contest: repo creado para este hackathon.
- [x] Platform: web app con backend V y dashboard Vue.
- [x] Google Cloud AI: Gemini configurable y Cloud Run deploy path V.
- [x] Partner track: Dynatrace.
- [x] MCP: adaptador Dynatrace MCP remoto con modo demo.
- [x] Agent behavior: planifica, usa herramientas, propone acciones y mantiene
  control humano.
- [x] No dependencia core de cloud competidor.
- [ ] Conectar token real Dynatrace y capturar evidencia, si hay acceso.
- [ ] Conectar Gemini real y capturar evidencia, si hay API key.

## Submission requirements

- [x] Hosted Project URL publica y estable:
  `https://jechaviz.github.io/google_cloud_rapid_agent_hackathon_web/`.
- [x] Public open-source repo URL:
  `https://github.com/jechaviz/google_cloud_rapid_agent_hackathon`.
- [x] License file visible: MIT.
- [ ] Text description con features, tecnologias, datos y aprendizajes.
- [ ] Demo video publico/no listado, aproximadamente 3 minutos.
- [ ] Video muestra el proyecto funcionando en web.
- [ ] Track seleccionado en Devpost: Dynatrace.
- [ ] Formulario Devpost completo.
- [ ] No logos, marcas, claims o materiales de terceros sin autorizacion.
- [ ] No contenido ofensivo, ilegal, discriminatorio o fuera del espiritu del
  hackathon.

## Judging alignment

- [x] Technological Implementation: Vlang core, Cloud Run, Gemini REST, MCP.
- [x] Design: dashboard Vue de triage con intake, metricas, topologia y plan.
- [x] Potential Impact: reduce MTTR, evidencia y postmortem.
- [x] Quality of Idea: incident agent con approval gate y audit trail.

## Final submit gate

- [x] Run tests.
- [x] Regenerar `evidence/v_agent_run.json`.
- [ ] Revisar screenshots/video por secretos.
- [ ] Confirmar Devpost draft.
- [ ] Ejecutar submit solo con confirmacion humana explicita.
