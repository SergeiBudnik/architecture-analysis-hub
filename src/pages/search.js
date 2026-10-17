import React, {useState} from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

const resources = [["A2A QR & Deep Link Payments","payments/a2a-qr-deeplink","a2a qr deeplink bank app callback orchestration"],["A2A Architecture Decisions","payments/a2a-design-decisions","hld payment design traceability"],["Card Acquiring & Processing","payments/acquiring-processing","acquirer gateway issuer network iso8583 reversal"],["Acquiring Decisions","payments/acquiring-design-decisions","authorization timeouts ADR"],["Clearing & Settlement","payments/clearing-settlement-reconciliation","capture presentment merchant payout ledger"],["Reconciliation Example","payments/reconciliation-worked-example","fees net gross bank mismatch"],["Settlement Decisions","payments/clearing-design-decisions","audit clearing file controls"],["Kafka Event-Driven Payments","payments/event-driven-processing","kafka consumer topic outbox inbox"],["Kafka Offset Recovery","payments/kafka-offset-recovery","consumer lag crash offset rebalance"],["Kafka Event Contracts","payments/event-driven-contracts","json schema sql postgres"],["Event-Driven ADRs","payments/event-driven-design-decisions","retry dead letter queue DLQ tests"],["Payment State Machine","payments/state-machine","idempotency lifecycle state"],["Timeout, Retry & Recovery","payments/reliability","failure status enquiry"],["PlantUML Diagrams","payments/diagrams","component sequence puml"],["BRD Template","templates/brd-template","business requirements stakeholders"],["SRS Template","templates/srs-template","software requirements functional nonfunctional"],["HLA Guide","templates/high-level-architecture-guide","HLD high level design components"],["Use Case Template","templates/use-case-template","user flow scenario"],["User Story Template","templates/user-story-template","agile acceptance"],["Database Design","templates/database-design-template","tables SQL ERD"],["Backend SRS","templates/backend-srs-template","REST processing"],["Frontend SRS","templates/frontend-srs-template","UI screens UX"],["Message Broker Spec","templates/message-broker-spec-template","MQ consumer"],["Integration Spec","templates/integration-specification","mapping API"],["Travel Booking BRD Example","examples/travel-platform-brd","filled business requirements"],["Employee Export API Example","examples/employee-export-api","XLSX export"],["Travel Plan Backend Example","examples/travel-plan-delete-backend","backend deletion"],["Word-compatible Downloads","downloads","RTF DOCX templates download"],["Architecture Diagram Gallery","diagram-gallery","visual diagrams hld"],["About the Author","about-the-author","Sergei Budnik"],["Feedback and Contributions","contribute","GitHub issues"]];

export default function Search(){
  const [query,setQuery] = useState('');
  const terms = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
  const matches = terms.length ? resources.filter(([title,path,keywords]) =>
    terms.every(term => (title+' '+path+' '+keywords).toLowerCase().includes(term))
  ) : resources;
  return (
    <Layout title="Resource Search" description="Search curated library resources by subject and title">
      <main className="container" style={{maxWidth:940,paddingTop:48,paddingBottom:56}}>
        <h1>Find a Resource</h1>
        <p>Find payment architecture cases, HLD and sequence diagrams, Kafka patterns, and system analysis templates.</p>
        <label htmlFor="search-entries"><strong>Search titles and topics</strong></label>
        <input id="search-entries" type="search" className="resourceSearchInput" value={query}
          onChange={e=>setQuery(e.target.value)} placeholder="Try: idempotency, settlement, BRD, Kafka" />
        <p style={{marginTop:16}}>{matches.length} matching resource{matches.length===1?'':'s'}</p>
        <div className="resourceGrid">{matches.map(([title,path,keywords])=>
          <article className="resourceResult" key={path}>
            <h3><Link to={'/docs/'+path}>{title}</Link></h3>
            <p>{keywords.replaceAll(' ',' · ')}</p>
          </article>
        )}</div>
        {!matches.length && <p>No matches. Try a broader topic or browse <Link to="/docs/templates/catalogue">the catalogue</Link>.</p>}
        <p style={{marginTop:22,fontSize:13,opacity:.75}}>This is a curated title/topic search, not a full-text index of every paragraph.</p>
      </main>
    </Layout>
  );
}
